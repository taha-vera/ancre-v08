import argparse, random, math, secrets, json, os
from datetime import datetime, timezone

def geo(p):
    u = secrets.randbelow(2**53)/(2**53)
    u = max(u, 1e-300)
    return max(1, math.ceil(math.log(u)/math.log(1-p)))

def dlap(scale_int):
    p = 1 - math.exp(-1/scale_int)
    return geo(p) - geo(p)

def pipeline(n, seed, epsilon=0.5, r=1000):
    random.seed(seed)
    signals = [random.uniform(0.3, 1.0) for _ in range(n)]
    K, alpha = 10, 0.1
    m = n // K
    blocks = [signals[i*m:(i+1)*m] for i in range(K)]
    means = [sum(b)/len(b) for b in blocks]
    t = max(1, int(alpha*K))
    trimmed = sorted(means)[t:-t]
    mu = sum(trimmed)/len(trimmed)
    n_eff = m*(K-2*t)
    si = max(1, round(r*2/(n_eff*epsilon)))
    result = mu + dlap(si)/r
    signals.clear()
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--runs', type=int, default=100)
    parser.add_argument('--epsilon', type=float, default=0.5)
    parser.add_argument('--n', type=int, default=100000)
    args = parser.parse_args()

    import time, statistics
    latencies = []
    for i in range(args.runs):
        t0 = time.time()
        pipeline(args.n, seed=42+i, epsilon=args.epsilon)
        latencies.append((time.time()-t0)*1000)

    latencies.sort()
    metrics = {
        "date": datetime.now(timezone.utc).isoformat(),
        "n": args.n,
        "runs": args.runs,
        "epsilon": args.epsilon,
        "p50_ms": round(latencies[int(args.runs*0.50)], 2),
        "p95_ms": round(latencies[int(args.runs*0.95)], 2),
        "p99_ms": round(latencies[int(args.runs*0.99)], 2),
        "mean_ms": round(statistics.mean(latencies), 2),
        "stdev_ms": round(statistics.stdev(latencies), 2)
    }
    print(f"p50={metrics['p50_ms']}ms p95={metrics['p95_ms']}ms p99={metrics['p99_ms']}ms")
    print(f"mean={metrics['mean_ms']}ms stdev={metrics['stdev_ms']}ms")
    os.makedirs("metrics", exist_ok=True)
    fname = f"metrics/ci_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Saved: {fname}")

if __name__ == '__main__':
    main()
