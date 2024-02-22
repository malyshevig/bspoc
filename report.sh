#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-Test-20231018.csv -d ./data/ignite -t "Apache Ignite"
#python3 /Users/im/PycharmProjects/bs/lp/report.py keydb-Test-20231117.csv -d ./data/results/keydb -t "KeyDB"
#python3 /Users/im/PycharmProjects/bs/lp/report.py KeyDB_RewriteOn_20231120.csv -d ./data/results/keydb_rewrite -t "KeyDB (aof rewrite)"
#python3 /Users/im/PycharmProjects/bs/lp/report.py RedisTest_20231106.csv -d ./data/results/redis -t "Redis"
#python3 /Users/im/PycharmProjects/bs/lp/report.py RedisTest-aofRewrite-20231103.csv -d ./data/results/redis_03_11 -t "Redis"
#python3 /Users/im/PycharmProjects/bs/lp/report.py RedisTest_NoPersistance.csv -d ./data/results/redis_no_pers -t "Redis"
#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis_RewriteOn_20231120.csv -d ./data/results/redis_rewrite -t "Redis (aof rewrite)"
#python3 /Users/im/PycharmProjects/bs/lp/report.py RedisRewriteTest_20231127.csv -d ./data/results/redis_rewrite_512 -t "Redis (aof rewrite, payload=512)"
#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis_Rewrite_256_20231128.csv -d ./data/results/redis_rewrite_256 -t "Redis (aof rewrite, payload=256)"
#python3 /Users/im/PycharmProjects/bs/lp/report.py RedisRDBReplicas.csv -d ./data/results/Redis_persistence_on_replicas -t "Redis (persistence on replicas)"

#python3 /Users/im/PycharmProjects/bs/lp/report.py RedisReplicaRDB_luaFix_1h.csv -d ./data/results/redis_pers_on_repl_lua -t "Redis (persistence on replicas Wait in lua)"
#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis_WaitReplica2_luaFix.csv -d ./data/results/redis_pers_on_repl_lua2 -t "Redis (persistence on replicas WaitReplicas=2 in lua)"


#python3 /Users/im/PycharmProjects/bs/lp/report.py ScyllaDB_test_20231115.csv -d ./data/results/scylladb -t "ScyllaDB"
#python3 /Users/im/PycharmProjects/bs/lp/report.py ScyllaDB_Test_20231114.csv -d ./data/results/scylladb_no_trn -t "ScyllaDB (trn turned off)"
#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-12hrs.csv -d ./data/results/tarantool -t "Tarantool"

#python3 /Users/im/PycharmProjects/bs/lp/report.py TarantoolTest_20240117.csv -d ./data/results/tarantool.2024-01-17 -t "Tarantool"
#python3 /Users/im/PycharmProjects/bs/lp/report.py TarantoolTest_20240117.csv -d ./data/results/tarantool.2024_01_17_1 -t "Tarantool" -s 2024-01-16_18.01.66_session_f5f31244
#python3 /Users/im/PycharmProjects/bs/lp/report.py TarantoolTest_20240117.csv -d ./data/results/tarantool.2024_01_18 -t "Tarantool" -s 2024-01-16_18.01.68_session_294752ff

#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-SaveSnap.csv -d ./data/results/tarantool.2024_01_18 -t "Tarantool" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-Random-2h.csv -w 15 -d ./data/results/tarantool.2024_01_18_2h_random -t "Tarantool (Random test)"

#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-saveSnap-every2h.csv -d ./data/results/tarantool_2024_01_19 -t "Tarantool" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-40RS.csv -d ./data/results/terantool_2024_01_20_40 -t "Tarantool (40 rs)" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-4Nbomber.csv -d ./data/results/tarantool_2024_01_22_max -t "Tarantool (40 rs, max)" -w 1
#python3 /Users/im/PycharmProjects/bs/lp/report.py Tarantool-RandomChoice.csv -d ./data/results/tarantool_2024_random -t "Tarantool Random Test" -w 30



#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-3Nbomber.csv -d ./data/results/ignite_21_01_2024 -t "Ignite" -w 15
#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-RandomChoice.csv -d ./data/results/ignite/ignite_2024_01_23_random -t "Ignite random" -w 15
#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-1h-Load.csv -d ./data/results/ignite/ignite_2024_01_23_1h -t "Ignite 1h" -w 15
#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-12h.csv -d ./data/results/ignite/ignite_2024_01_24 -t "Ignite 1h" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-12h-NoWal.csv -d ./data/results/ignite/ignite_2024_01_25_no_wal -t "Ignite NoWal" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-12h-newConf.csv -d ./data/results/ignite/ignite_2024_01_29_12h -t "Ignite Optimized Persistence" -w 45
#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-12h-extref.csv -d ./data/results/ignite/ignite_2024_02_01_12H -t "Ignite 12h test" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Ignite-RandomChoice-extref.csv -d ./data/results/ignite/ignite_2024_02_01_random -t "Ignite Random" -w 45


#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-RandomTest-AOF_RDB.csv -d ./data/results/redis_2024_01_30_random -t "Redis Random Test" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis_Master_GraceShutdown_20231205.csv -d ./data/results/redis_master_grace_shutdown -t "Redis Master Graceful Shutdown"
#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis_TestAOF_replica_20231205.csv -d ./data/results/Redis_persistence_aof_on_replicas -t "Redis (persistence with aof rewrites)"

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-AddNewNode.csv -d ./data/results/redis_failover_06_02 -t "Redis (Add Node)" -w 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis_Rewrite_killReplica1_chg.csv -d ./data/results/redis_kill_replica1 -t Redis -w 1
#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-Rewrite-killReplica2_chg.csv -d ./data/results/redis_kill_replica2 -t Redis -w 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-Rewrite-killMaster.csv -d ./data/results/redis_killmaster -t Redis -w 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-18Shards-12h.csv -d ./data/results/redis_2024_02_09_18_Shards -t "Redis 18 shards" -w 45

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-18shards-MasterRDB.csv -d ./data/results/redis_18shard_master_rdb -t "Redis 18 shards" -w 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-27Shards.csv -d ./data/results/redis_27shard_master_rdb -t "Redis 27 shards" -w 45


#python3 /Users/im/PycharmProjects/bs/lp/report.py Master_ForceShutdown.csv -d ./data/results/redis_master_forced_shutdown -t "Redis 27 shards" -w 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-36Shards-12h.csv -d ./data/results/redis_36shard_12h -t "Redis 36 shards" -w 45 -r 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-45shards-12h.csv -d ./data/results/redis_2024_02_14_45_shards -t "Redis 45 shards" -w 45 -r 1


#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-45shards-RDB.csv -d ./data/results/redis_2024_02_14_45_shards_rdb -t "Redis 45 shards" -w 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-99shards-12h.csv -d ./data/results/redis_99shards_12h -t "Redis 99 shards" -w 45 -r 15

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-198shards-12h.csv -d ./data/results/redis_2024_02_15_198shards -t "Redis 198 shards" -w 45 -r 15

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-198shards-RDB.csv -d ./data/results/redis_2024_02_15_198shards_rdb -t "Redis 99 shards" -w 1 -r 1

#python3 /Users/im/PycharmProjects/bs/lp/report.py Redis-CPUAff-12h.csv -d ./data/results/redis_2024_02_19_CPUAff-12h -t "Redis CPU Affinity" -w 45 -r 5

python report.py Redis-TLS-12h.csv -d ./data/redis/redis_tls_12h -t "Redis TLS " -w 45 -r 5


