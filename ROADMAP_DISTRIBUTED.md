# Roadmap — Distributed Evaluation

## Ce qu'on a maintenant
- 3 rôles P1/P2/P3 séparés
- Vraie communication TCP
- Métriques persistées
- Pipeline reproductible

## Ce qu'on n'a PAS encore
- MPC cryptographique
- Streaming chunked (pas batch JSON)
- Protocol binaire (pas JSON)
- Async runtime

## Terminologie correcte
PAS : "real MPC"
OUI : "three-party distributed aggregation pipeline"
OUI : "multi-party validation architecture"

## Étape 1 — Métriques p50/p95/p99
- sustained load 5min
- chunk sizes variés
- sérialisation cost mesuré

## Étape 2 — Injection réseau
tc qdisc add dev eth0 root netem delay 50ms loss 2%

## Étape 3 — Crash recovery
- kill P3 → observer comportement
- restart P3 → mesurer recovery time

## Étape 4 — Rust/Tokio transport
- Remplacer Python sockets
- Async multiplexing
- Backpressure
- → Vrai paper CCS distribué

## Ce qui est publiable maintenant
"Bounded-memory streaming aggregation
under distributed coordination constraints"
→ PETS borderline accept
