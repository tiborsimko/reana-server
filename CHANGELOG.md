<!-- markdownlint-disable MD013 -->

# Changelog

## [0.95.0](https://github.com/tiborsimko/reana-server/compare/v0.9.4...0.95.0) (2025-06-29)


### ⚠ BREAKING CHANGES

* **python:** drop support for Python 3.6 and 3.7
* **gitlab:** The REST API endpoint `gitlab_projects` now includes pagination details.

### Build

* **deps:** pin invenio-userprofiles to 1.2.4 ([#665](https://github.com/tiborsimko/reana-server/issues/665)) ([d6cb168](https://github.com/tiborsimko/reana-server/commit/d6cb16854aea78d852ab43987a44933a9d6fbcad))
* **docker:** non-editable submodules in "latest" mode ([#656](https://github.com/tiborsimko/reana-server/issues/656)) ([d16fefb](https://github.com/tiborsimko/reana-server/commit/d16fefb421e1d0cc712006c6a697ea67057b1f6c))
* **docker:** pin setuptools to v70 ([#696](https://github.com/tiborsimko/reana-server/issues/696)) ([c1b4b71](https://github.com/tiborsimko/reana-server/commit/c1b4b710fee23c2215a5a884bedbd00c90881596))
* **docker:** upgrade to Ubuntu 24.04 and Python 3.12 ([#692](https://github.com/tiborsimko/reana-server/issues/692)) ([091a9ed](https://github.com/tiborsimko/reana-server/commit/091a9ed327b4f7a28f16e89bab46110c0a463749))
* **python:** add minimal `pyproject.toml` ([#696](https://github.com/tiborsimko/reana-server/issues/696)) ([6313720](https://github.com/tiborsimko/reana-server/commit/631372081660d7c8e831b351c3db0123cc76c911))
* **python:** bump all required packages as of 2024-03-04 ([#674](https://github.com/tiborsimko/reana-server/issues/674)) ([f40b82f](https://github.com/tiborsimko/reana-server/commit/f40b82f983d295348a4a5a537b4147a9dc8b6dae))
* **python:** bump shared modules ([#676](https://github.com/tiborsimko/reana-server/issues/676)) ([47ad3ca](https://github.com/tiborsimko/reana-server/commit/47ad3caab04119568b0f790075784aae59c3818d))
* **python:** bump shared REANA packages as of 2024-03-04 ([#674](https://github.com/tiborsimko/reana-server/issues/674)) ([aa18394](https://github.com/tiborsimko/reana-server/commit/aa18394458d56806913e224e1b6651a177d18b39))
* **python:** bump shared REANA packages as of 2024-11-28 ([#714](https://github.com/tiborsimko/reana-server/issues/714)) ([94fbf77](https://github.com/tiborsimko/reana-server/commit/94fbf7766218f4ffaf3f23be64ec6d46be1acb00))
* **python:** drop support for Python 3.6 and 3.7 ([#683](https://github.com/tiborsimko/reana-server/issues/683)) ([868dee9](https://github.com/tiborsimko/reana-server/commit/868dee9330bf28727f550965416ab6c670d32f9d))
* **python:** remove deprecated `pytest-runner` ([#696](https://github.com/tiborsimko/reana-server/issues/696)) ([20431fe](https://github.com/tiborsimko/reana-server/commit/20431fe5f3fc0e451afa1f4f8e6734bd41b84acc))
* **python:** use optional deps instead of `tests_require` ([#696](https://github.com/tiborsimko/reana-server/issues/696)) ([9c2a31f](https://github.com/tiborsimko/reana-server/commit/9c2a31f154c4d60d5a1887ca69d7f30525d482f4))


### Features

* **api:** add workflow engine versions to info endpoint ([#711](https://github.com/tiborsimko/reana-server/issues/711)) ([999d716](https://github.com/tiborsimko/reana-server/commit/999d71667827dc420ab57ef3c2cca8417622fa65))
* **config:** make ACCOUNTS_USERINFO_HEADERS customisable ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([8c01d51](https://github.com/tiborsimko/reana-server/commit/8c01d513c2365f337c26a2211c2ddb82df4186d4))
* **config:** make APP_DEFAULT_SECURE_HEADERS customisable ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([1919358](https://github.com/tiborsimko/reana-server/commit/1919358cb3b05f09bceff9a904e9607760bc3fb1))
* **config:** make Dask autoscaler configurable ([#702](https://github.com/tiborsimko/reana-server/issues/702)) ([95ea2df](https://github.com/tiborsimko/reana-server/commit/95ea2df5a56177b804ac41e97e3c90ab7e89ce2d))
* **config:** make number of threads configurable for Dask ([#719](https://github.com/tiborsimko/reana-server/issues/719)) ([5b82925](https://github.com/tiborsimko/reana-server/commit/5b8292541b10126823da8a288dbc3e87591724c0))
* **config:** make PROXYFIX_CONFIG customisable ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([5b6c276](https://github.com/tiborsimko/reana-server/commit/5b6c276f57f642cc0965f096fa59875b9599df08))
* **config:** set maximum limit for number of Dask workers ([#712](https://github.com/tiborsimko/reana-server/issues/712)) ([d36b59b](https://github.com/tiborsimko/reana-server/commit/d36b59bece781b2c4d11b20ea0d9a47630ef2601))
* **config:** support password-protected redis ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([a2aad8a](https://github.com/tiborsimko/reana-server/commit/a2aad8ac506b98e5c29d357cec65172b6437cc8f))
* **ext:** improve error message for db decryption error ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([bbab1bf](https://github.com/tiborsimko/reana-server/commit/bbab1bf7338e9790e2195a02e320df16db1826f6))
* **gitlab:** add search query parameter to filter projects ([#681](https://github.com/tiborsimko/reana-server/issues/681)) ([109cf38](https://github.com/tiborsimko/reana-server/commit/109cf38be440e15676e53ec1458ff9efe7d4a395)), closes [#518](https://github.com/tiborsimko/reana-server/issues/518)
* **gitlab:** add support for paginated project list ([#681](https://github.com/tiborsimko/reana-server/issues/681)) ([4d23c62](https://github.com/tiborsimko/reana-server/commit/4d23c62d57b8ada0d12895fe03190b898b4abd61)), closes [#518](https://github.com/tiborsimko/reana-server/issues/518)
* **helm:** add initial Dask support ([#701](https://github.com/tiborsimko/reana-server/issues/701)) ([15d0b97](https://github.com/tiborsimko/reana-server/commit/15d0b97a7cc30364bc09870a2bebfef4264e94a0))
* **rest:** add `live_logs_enabled` property in logs output ([#705](https://github.com/tiborsimko/reana-server/issues/705)) ([c4be985](https://github.com/tiborsimko/reana-server/commit/c4be9854b7817fd6d8b03f06e33948d861e9721a))
* **rest:** add endpoint for sharing workflows ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([045d275](https://github.com/tiborsimko/reana-server/commit/045d2752cce08956c73ed14983ff5d6519dc149d))
* **rest:** add endpoint to get workflow share status ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([b7d14bb](https://github.com/tiborsimko/reana-server/commit/b7d14bb83284f3f577f096b4110324ec07904651))
* **rest:** add endpoint to unshare workflows ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([727c04e](https://github.com/tiborsimko/reana-server/commit/727c04ef7f0a5cfc26f1f2af4213933efcab38f6))
* **rest:** add endpoints to fetch sharing users ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([3a1c5ea](https://github.com/tiborsimko/reana-server/commit/3a1c5ea900afb850f5c5e2e4fe0b69275480b9b1))
* **rest:** add share-related parameters to `get_workflows` ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([a72f1ac](https://github.com/tiborsimko/reana-server/commit/a72f1ac1a95311ef1e048c271b923cc511cf0ac9))
* **rest:** add user id to get-you endpoint ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([20246c9](https://github.com/tiborsimko/reana-server/commit/20246c956d1458851212130a7ed1f214bae9ba1f))
* **rest:** make details available for shared workflows ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([b274a29](https://github.com/tiborsimko/reana-server/commit/b274a2995fefa0bb1601529bfb05aaa058580205))
* **sessions:** add recommended images to info endpoint ([#688](https://github.com/tiborsimko/reana-server/issues/688)) ([908aca2](https://github.com/tiborsimko/reana-server/commit/908aca26c4a523bff285ef414bd9a8cb9eba064b))


### Bug fixes

* **config:** do not set DEBUG programmatically ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([c98cbc1](https://github.com/tiborsimko/reana-server/commit/c98cbc1d15afca9309e4839db543ac19cd2036ce))
* **config:** read secret key from env ([#713](https://github.com/tiborsimko/reana-server/issues/713)) ([6ee6422](https://github.com/tiborsimko/reana-server/commit/6ee6422d87d38339b359ad7a306575b97f210440))
* **config:** set localhost default value for REANA_HOSTNAME ([#717](https://github.com/tiborsimko/reana-server/issues/717)) ([a24c810](https://github.com/tiborsimko/reana-server/commit/a24c810f018e5fd925d9ad01ce986537adad7ee8))
* **flask:** avoid deprecated decorator `before_first_request` ([#692](https://github.com/tiborsimko/reana-server/issues/692)) ([6d3fe7d](https://github.com/tiborsimko/reana-server/commit/6d3fe7dcf83ef1fea42dcaae0a15b2b83b4a5e10))
* **get_workflow_specification:** avoid returning null parameters ([#689](https://github.com/tiborsimko/reana-server/issues/689)) ([46633d6](https://github.com/tiborsimko/reana-server/commit/46633d6bcc151c73880f9ecbd2c02d2246492794))
* **gitlab:** handle pagination of GitLab webhooks ([#684](https://github.com/tiborsimko/reana-server/issues/684)) ([3f716f7](https://github.com/tiborsimko/reana-server/commit/3f716f7369230ab2a864b6bfcae44a952ca5bf90)), closes [#682](https://github.com/tiborsimko/reana-server/issues/682)
* **reana-admin:** respect service domain when cleaning sessions ([#687](https://github.com/tiborsimko/reana-server/issues/687)) ([ede882d](https://github.com/tiborsimko/reana-server/commit/ede882d384ae0959eb8a9484b7d491baa628a1ee))
* **reana-admin:** skip retention rules for deleted workspaces ([#697](https://github.com/tiborsimko/reana-server/issues/697)) ([d1cd1a5](https://github.com/tiborsimko/reana-server/commit/d1cd1a5a593323ba74d8a8053bab32e4a7d903a1))
* **rest:** fix workflow sharing endpoints after changes ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([50495fc](https://github.com/tiborsimko/reana-server/commit/50495fc8a2eca691357eaa307ed3580ed7aac91d))
* **set_workflow_status:** publish workflows to submission queue ([#691](https://github.com/tiborsimko/reana-server/issues/691)) ([6e35bd7](https://github.com/tiborsimko/reana-server/commit/6e35bd776e17c1bc04145c68c1f5ea3ce5143b7e)), closes [#690](https://github.com/tiborsimko/reana-server/issues/690)
* **start:** validate endpoint parameters ([#689](https://github.com/tiborsimko/reana-server/issues/689)) ([d2d3673](https://github.com/tiborsimko/reana-server/commit/d2d3673dac8917d746ddafd84bb3660e7f83c9b6))


### Code refactoring

* **docs:** move from reST to Markdown ([#671](https://github.com/tiborsimko/reana-server/issues/671)) ([b6d1799](https://github.com/tiborsimko/reana-server/commit/b6d1799552085e1a9c2ad53eafcd572f1af4f3bf))
* **gitlab:** move all GitLab requests to dedicated client ([#685](https://github.com/tiborsimko/reana-server/issues/685)) ([703af19](https://github.com/tiborsimko/reana-server/commit/703af19e4232af5c9b3ecdefb0b90a60e796605c)), closes [#676](https://github.com/tiborsimko/reana-server/issues/676)
* **secrets:** adapt to reana-commons secret-handling changes ([#686](https://github.com/tiborsimko/reana-server/issues/686)) ([3596ee0](https://github.com/tiborsimko/reana-server/commit/3596ee058a9888d723a8fcd6247bb14ff1095821))


### Code style

* **black:** format with black v24 ([#670](https://github.com/tiborsimko/reana-server/issues/670)) ([6d2b898](https://github.com/tiborsimko/reana-server/commit/6d2b898b2322e6677739fdb1c3bd3916a3cf0887))


### Test suite

* **pytest:** adapt to fixture changes from default_user to user0 ([#658](https://github.com/tiborsimko/reana-server/issues/658)) ([72a6964](https://github.com/tiborsimko/reana-server/commit/72a6964de3c232f23e2f6a9321b98a3a859e2364))


### Continuous integration

* **actions:** update GitHub actions due to Node 16 deprecation ([#680](https://github.com/tiborsimko/reana-server/issues/680)) ([b7cc00a](https://github.com/tiborsimko/reana-server/commit/b7cc00afddb5035a3ed8f964ea33fb94bca3e2d8))
* add hadolint and flake8 linters ([b78d62d](https://github.com/tiborsimko/reana-server/commit/b78d62d77d918498c88f48f9425fe0c1e3cf80b9))
* added github actions workflow ([247e3a3](https://github.com/tiborsimko/reana-server/commit/247e3a3adfcf298312fd7e85efc60aaf1bc2437d))
* **commitlint:** addition of commit message linter ([#665](https://github.com/tiborsimko/reana-server/issues/665)) ([2b43ecc](https://github.com/tiborsimko/reana-server/commit/2b43eccdd7587970f92093b4d315a7a90b5f45ac))
* **commitlint:** allow release commit style ([#675](https://github.com/tiborsimko/reana-server/issues/675)) ([e0299ef](https://github.com/tiborsimko/reana-server/commit/e0299efb273f2c95f88f86261c97a4bc6100786d))
* **commitlint:** check for the presence of concrete PR number ([#669](https://github.com/tiborsimko/reana-server/issues/669)) ([87c6145](https://github.com/tiborsimko/reana-server/commit/87c6145e636d852ba5fd5ca6fa2cfc23ff6563d2))
* **commitlint:** fix local running of commit linter on macOS ([#736](https://github.com/tiborsimko/reana-server/issues/736)) ([40b5356](https://github.com/tiborsimko/reana-server/commit/40b535698c9200d61eb62cf53c29d5f918cc5c25))
* **commitlint:** improve checking of merge commits ([#689](https://github.com/tiborsimko/reana-server/issues/689)) ([69f45fc](https://github.com/tiborsimko/reana-server/commit/69f45fc3aae9bc625ed733de9af13eb7c0111048))
* **commitlint:** improve checking of merge commits ([#692](https://github.com/tiborsimko/reana-server/issues/692)) ([9a7bd8c](https://github.com/tiborsimko/reana-server/commit/9a7bd8c94b76c0a7942b3f3cbae671fde334e49b))
* **jsonlint:** add JSON linting ([#732](https://github.com/tiborsimko/reana-server/issues/732)) ([cc3753a](https://github.com/tiborsimko/reana-server/commit/cc3753a522b732ff3c6f3d5ae90262551577cdd6))
* **markdownlint:** add Markdown linting ([#735](https://github.com/tiborsimko/reana-server/issues/735)) ([d05e5af](https://github.com/tiborsimko/reana-server/commit/d05e5affe0de3153d56183fb8d1ca83b17daad95))
* pin hadolint version ([2bd2bd4](https://github.com/tiborsimko/reana-server/commit/2bd2bd497dd96c41449f31af9086ee1670bff8df))
* **prettier:** add Prettier code formatting checks ([#737](https://github.com/tiborsimko/reana-server/issues/737)) ([e04d1fd](https://github.com/tiborsimko/reana-server/commit/e04d1fdd679bc576e685ca0bab978594da775c35))
* publish docker image after new release ([34131ba](https://github.com/tiborsimko/reana-server/commit/34131bae5506785fc918047fdfdde5c8fb92833b))
* **pytest:** invoke `pytest` directly instead of `setup.py test` ([#696](https://github.com/tiborsimko/reana-server/issues/696)) ([bd6762f](https://github.com/tiborsimko/reana-server/commit/bd6762fc3ef1a79d5354ac167e0e08383eec9d6c))
* **pytest:** move to PostgreSQL 14.10 ([#672](https://github.com/tiborsimko/reana-server/issues/672)) ([e888ddd](https://github.com/tiborsimko/reana-server/commit/e888ddd70d8ca17d4567c24b7d78a57bf6f8e060))
* **release-please:** initial configuration ([#665](https://github.com/tiborsimko/reana-server/issues/665)) ([1d5e7c5](https://github.com/tiborsimko/reana-server/commit/1d5e7c5f4c3d471d0b2028274ec1785b53552d89))
* **release-please:** update version in Dockerfile/OpenAPI specs ([#668](https://github.com/tiborsimko/reana-server/issues/668)) ([3b3dc41](https://github.com/tiborsimko/reana-server/commit/3b3dc418f40d5ce461e4a7418178f6a8cec2721f))
* remove older versions from python tests ([28454b9](https://github.com/tiborsimko/reana-server/commit/28454b9741b3a000268cc6a87ea271e4c07588e2))
* removed pip upgrade ([a6694fa](https://github.com/tiborsimko/reana-server/commit/a6694fa19a355541321d89c3151ca97fd1f5c633))
* **shellcheck:** fix exit code propagation ([#669](https://github.com/tiborsimko/reana-server/issues/669)) ([d7eac6b](https://github.com/tiborsimko/reana-server/commit/d7eac6b26742797cb1b2c7077071fc3d2053aff1))
* **shfmt:** add shfmt code formatting checks ([#734](https://github.com/tiborsimko/reana-server/issues/734)) ([1dcc563](https://github.com/tiborsimko/reana-server/commit/1dcc56380adc5987d2ba9becd2de643166542038))
* update all actions ([b72bc72](https://github.com/tiborsimko/reana-server/commit/b72bc727adaa87e371d982b5e9f20f9361ecbc12))
* **yamllint:** add YAML linting ([#733](https://github.com/tiborsimko/reana-server/issues/733)) ([c36c461](https://github.com/tiborsimko/reana-server/commit/c36c461352cb19ff3f8b9f2901d7520482065e12))


### Documentation

* add .readthedocs.yaml to migrate to RTD v2 ([cf1ecd5](https://github.com/tiborsimko/reana-server/commit/cf1ecd5baec4d792c03b9eac578f69386ddcad68))
* **authors:** complete list of contributors ([#673](https://github.com/tiborsimko/reana-server/issues/673)) ([71b3f38](https://github.com/tiborsimko/reana-server/commit/71b3f387b0816e23a3315c379ed45af0bb6661a3))
* remove reana-cluster references ([6255db8](https://github.com/tiborsimko/reana-server/commit/6255db82ddac882a2acef8e909465c256dd6684d))
* set language to English ([cc7bafa](https://github.com/tiborsimko/reana-server/commit/cc7bafa6c40ad216631bc7ed7665625a4e37e8d4))
* single-page RTFD outline ([231e0d5](https://github.com/tiborsimko/reana-server/commit/231e0d56626087962391c380e3446a807bc2a927))
* update openapi.json ([2453cdc](https://github.com/tiborsimko/reana-server/commit/2453cdc77b31a2fd9ca3e4ab5f52fc36df509eaa))


### Chores

* **master:** release 0.95.0-alpha.1 ([9fa4059](https://github.com/tiborsimko/reana-server/commit/9fa40595ce840391c4aed999c3d4dda4de7ad2eb))

## [0.9.4](https://github.com/reanahub/reana-server/compare/0.9.3...0.9.4) (2024-11-29)

### Build

* **python:** bump shared REANA packages as of 2024-11-28 ([#714](https://github.com/reanahub/reana-server/issues/714)) ([94fbf77](https://github.com/reanahub/reana-server/commit/94fbf7766218f4ffaf3f23be64ec6d46be1acb00))

### Features

* **config:** make ACCOUNTS_USERINFO_HEADERS customisable ([#713](https://github.com/reanahub/reana-server/issues/713)) ([8c01d51](https://github.com/reanahub/reana-server/commit/8c01d513c2365f337c26a2211c2ddb82df4186d4))
* **config:** make APP_DEFAULT_SECURE_HEADERS customisable ([#713](https://github.com/reanahub/reana-server/issues/713)) ([1919358](https://github.com/reanahub/reana-server/commit/1919358cb3b05f09bceff9a904e9607760bc3fb1))
* **config:** make PROXYFIX_CONFIG customisable ([#713](https://github.com/reanahub/reana-server/issues/713)) ([5b6c276](https://github.com/reanahub/reana-server/commit/5b6c276f57f642cc0965f096fa59875b9599df08))
* **config:** support password-protected redis ([#713](https://github.com/reanahub/reana-server/issues/713)) ([a2aad8a](https://github.com/reanahub/reana-server/commit/a2aad8ac506b98e5c29d357cec65172b6437cc8f))
* **ext:** improve error message for db decryption error ([#713](https://github.com/reanahub/reana-server/issues/713)) ([bbab1bf](https://github.com/reanahub/reana-server/commit/bbab1bf7338e9790e2195a02e320df16db1826f6))

### Bug fixes

* **config:** do not set DEBUG programmatically ([#713](https://github.com/reanahub/reana-server/issues/713)) ([c98cbc1](https://github.com/reanahub/reana-server/commit/c98cbc1d15afca9309e4839db543ac19cd2036ce))
* **config:** read secret key from env ([#713](https://github.com/reanahub/reana-server/issues/713)) ([6ee6422](https://github.com/reanahub/reana-server/commit/6ee6422d87d38339b359ad7a306575b97f210440))
* **get_workflow_specification:** avoid returning null parameters ([#689](https://github.com/reanahub/reana-server/issues/689)) ([46633d6](https://github.com/reanahub/reana-server/commit/46633d6bcc151c73880f9ecbd2c02d2246492794))
* **reana-admin:** respect service domain when cleaning sessions ([#687](https://github.com/reanahub/reana-server/issues/687)) ([ede882d](https://github.com/reanahub/reana-server/commit/ede882d384ae0959eb8a9484b7d491baa628a1ee))
* **set_workflow_status:** publish workflows to submission queue ([#691](https://github.com/reanahub/reana-server/issues/691)) ([6e35bd7](https://github.com/reanahub/reana-server/commit/6e35bd776e17c1bc04145c68c1f5ea3ce5143b7e)), closes [#690](https://github.com/reanahub/reana-server/issues/690)
* **start:** validate endpoint parameters ([#689](https://github.com/reanahub/reana-server/issues/689)) ([d2d3673](https://github.com/reanahub/reana-server/commit/d2d3673dac8917d746ddafd84bb3660e7f83c9b6))

### Continuous integration

* **commitlint:** improve checking of merge commits ([#689](https://github.com/reanahub/reana-server/issues/689)) ([69f45fc](https://github.com/reanahub/reana-server/commit/69f45fc3aae9bc625ed733de9af13eb7c0111048))

## [0.9.3](https://github.com/reanahub/reana-server/compare/0.9.2...0.9.3) (2024-03-04)

### Build

* **deps:** pin invenio-userprofiles to 1.2.4 ([#665](https://github.com/reanahub/reana-server/issues/665)) ([d6cb168](https://github.com/reanahub/reana-server/commit/d6cb16854aea78d852ab43987a44933a9d6fbcad))
* **docker:** non-editable submodules in "latest" mode ([#656](https://github.com/reanahub/reana-server/issues/656)) ([d16fefb](https://github.com/reanahub/reana-server/commit/d16fefb421e1d0cc712006c6a697ea67057b1f6c))
* **python:** bump all required packages as of 2024-03-04 ([#674](https://github.com/reanahub/reana-server/issues/674)) ([f40b82f](https://github.com/reanahub/reana-server/commit/f40b82f983d295348a4a5a537b4147a9dc8b6dae))
* **python:** bump shared modules ([#676](https://github.com/reanahub/reana-server/issues/676)) ([47ad3ca](https://github.com/reanahub/reana-server/commit/47ad3caab04119568b0f790075784aae59c3818d))
* **python:** bump shared REANA packages as of 2024-03-04 ([#674](https://github.com/reanahub/reana-server/issues/674)) ([aa18394](https://github.com/reanahub/reana-server/commit/aa18394458d56806913e224e1b6651a177d18b39))

### Code refactoring

* **docs:** move from reST to Markdown ([#671](https://github.com/reanahub/reana-server/issues/671)) ([b6d1799](https://github.com/reanahub/reana-server/commit/b6d1799552085e1a9c2ad53eafcd572f1af4f3bf))

### Code style

* **black:** format with black v24 ([#670](https://github.com/reanahub/reana-server/issues/670)) ([6d2b898](https://github.com/reanahub/reana-server/commit/6d2b898b2322e6677739fdb1c3bd3916a3cf0887))

### Continuous integration

* **commitlint:** addition of commit message linter ([#665](https://github.com/reanahub/reana-server/issues/665)) ([2b43ecc](https://github.com/reanahub/reana-server/commit/2b43eccdd7587970f92093b4d315a7a90b5f45ac))
* **commitlint:** allow release commit style ([#675](https://github.com/reanahub/reana-server/issues/675)) ([e0299ef](https://github.com/reanahub/reana-server/commit/e0299efb273f2c95f88f86261c97a4bc6100786d))
* **commitlint:** check for the presence of concrete PR number ([#669](https://github.com/reanahub/reana-server/issues/669)) ([87c6145](https://github.com/reanahub/reana-server/commit/87c6145e636d852ba5fd5ca6fa2cfc23ff6563d2))
* **pytest:** move to PostgreSQL 14.10 ([#672](https://github.com/reanahub/reana-server/issues/672)) ([e888ddd](https://github.com/reanahub/reana-server/commit/e888ddd70d8ca17d4567c24b7d78a57bf6f8e060))
* **release-please:** initial configuration ([#665](https://github.com/reanahub/reana-server/issues/665)) ([1d5e7c5](https://github.com/reanahub/reana-server/commit/1d5e7c5f4c3d471d0b2028274ec1785b53552d89))
* **release-please:** update version in Dockerfile/OpenAPI specs ([#668](https://github.com/reanahub/reana-server/issues/668)) ([3b3dc41](https://github.com/reanahub/reana-server/commit/3b3dc418f40d5ce461e4a7418178f6a8cec2721f))
* **shellcheck:** fix exit code propagation ([#669](https://github.com/reanahub/reana-server/issues/669)) ([d7eac6b](https://github.com/reanahub/reana-server/commit/d7eac6b26742797cb1b2c7077071fc3d2053aff1))

### Documentation

* **authors:** complete list of contributors ([#673](https://github.com/reanahub/reana-server/issues/673)) ([71b3f38](https://github.com/reanahub/reana-server/commit/71b3f387b0816e23a3315c379ed45af0bb6661a3))

## 0.9.2 (2023-12-12)

* Adds automated multi-platform container image building for amd64 and arm64 architectures.
* Adds metadata labels to Dockerfile.
* Changes workflow scheduler logging behaviour to also report the main reason behind scheduling errors to the users.
* Fixes runtime uWSGI warning by rebuilding uWSGI with the PCRE support.

## 0.9.1 (2023-09-27)

* Adds new `prune_workspace` endpoint to allow users to delete all the files of a workflow, specifying whether to also delete the inputs and/or the outputs.
* Adds new `interactive-session-cleanup` command that can be used by REANA administrators to close interactive sessions that are inactive for more than the specified number of days.
* Adds logic to support SSO with third-party Keycloak authentication services.
* Adds the timestamp of when the workflow was stopped (`run_stopped_at`) to the workflow list and the workflow status endpoints.
* Adds the content of the `REANA_GITLAB_HOST` environment variable to the list of GitLab instances from which it is possible to launch a workflow.
* Adds progress meter to the logs of the periodic quota updater.
* Changes CPU and disk quota calculations to improve the performance of periodic quota updater.
* Changes the system status report to simplify and clarify the disk usage summary.
* Changes `check-workflows` command to also check the presence of workspaces on the shared volume.
* Changes `check-workflows` command to not show in-sync runs by default. If needed, they can be shown using the new `--show-all` option.
* Changes `launch` endpoint to also include the warnings of the validation of the workflow specification.
* Changes OpenAPI specification of the `info` endpoint to return the maximum inactivity time before automatic closure of interactive sessions.
* Changes `apispec` dependency version in order to be compatible with `PyYAML` v6.
* Changes `reana-admin` command options to require the passing of `--admin-access-token` argument more globally.
* Fixes the workflow priority calculation to avoid workflows stuck in the `queued` status when the number of allowed concurrent workflow is set to zero.
* Fixes GitLab integration to automatically redirect the user to the correct URL when the access request is accepted.
* Fixes `quota-set-default-limits` command to propagate default quota limits to all users without custom quota limit values.
* Fixes authentication flow to correctly deny access to past revoked tokens in case the same user has also other new active tokens.
* Fixes email templates to show the correct `kubectl` commands when REANA is deployed inside a non-default namespace or with a custom component name prefix.
* Fixes email sender for system emails to `notifications.email_config.sender` Helm value.
* Fixes email receiver for token request emails to use `notifications.email_config.receiver` Helm value.
* Fixes `start-scheduler` command to gracefully stop when being terminated.
* Fixes container image names to be Podman-compatible.

## 0.9.0 (2023-01-19)

* Adds new `/api/launch` endpoint that allows running workflows from remote sources.
* Adds new `get_workflow_retention_rules` endpoint that allows to retrieve the workspace file retention rules of a workflow.
* Adds `queue-consume` command that can be used by REANA administrators to remove specific messages from the queue.
* Adds configuration environment variable to set an API rate limit for slow endpoints (`REANA_RATELIMIT_SLOW`).
* Adds REANA specification validation utilities.
* Adds `retention-rules-apply` command that can be used by REANA administrators to apply pending retention rules.
* Adds `retention-rules-extend` command that can be used by REANA administrators to extend the duration of active retentions rules.
* Adds `check-workflows` command that can be used by REANA administrators to check for out-of-sync workflows and interactive sessions.
* Changes OpenAPI specification to include missing response schema elements and some other small enhancements.
* Changes `/api/info` endpoint to also include the kubernetes maximum memory limit, the kubernetes default memory limit and the maximum workspace retention period.
* Changes `start_workflow` endpoint to validate the REANA specification of the workflow.
* Changes `create_workflow` endpoint to populate workspace retention rules for the workflow.
* Changes `start_workflow` endpoint to disallow restarting a workflow when retention rules are pending.
* Changes API rate limiter error messages to be more verbose.
* Changes workflow scheduler to allow defining the checks needed to assess whether the cluster can start new workflows.
* Changes the Invenio dependencies to the latest versions.
* Changes OAuth configuration to enable the new CERN SSO.
* Changes to PostgreSQL 12.13.
* Changes GitLab integration to also retrieve user's projects that are in groups and subgroups.
* Changes the base image of the component to Ubuntu 20.04 LTS and reduces final Docker image size by removing build-time dependencies.
* Fixes issue when irregular number formats are passed to `REANA_SCHEDULER_REQUEUE_COUNT` configuration environment variable.
* Fixes GitLab integration error reporting in case user exceeds CPU or Disk quota usage limits.
* Fixes CERN OIDC authentication to possibly allow eduGAIN and social login users.

## 0.8.4 (2022-02-23)

* Changes workflow scheduler to count number of workflow retries.

## 0.8.3 (2022-02-10)

* Adds Kubernetes job memory limits validation before publishing workflow submission.

## 0.8.2 (2022-02-07)

* Adds email validation to the `user-create` command used by the REANA administrators.
* Adds workflow name validation to the `create_workflow` endpoint.
* Changes `/api/info` endpoint to return a list of supported compute backends.
* Changes `/api/status` endpoint to calculate the cluster health status based on the availablity instead of the usage.

## 0.8.1 (2021-11-29)

* Changes `quota-set` command used by the REANA administrators to use the resource type along with a resource name for specifying the resource.
* Changes email validation used in `create-admin-user` command by the REANA administrators to be more permissive.

## 0.8.0 (2021-11-22)

* Adds users quota accounting.
* Adds support for Snakemake workflow engine.
* Adds `include_progress` and `include_workspace_size` query args to workflow list endpoint.
* Adds workflow prioritization in the queue by complexity.
* Adds `priority` and `min_job_memory` params to workflow submission publisher.
* Adds Yadage workflow specification loading to `start_workflow` endpoint.
* Adds a check in scheduler if at least one workflow job could be started in Kubernetes.
* Adds configuration environment variable to set workflow scheduling policy (`REANA_WORKFLOW_SCHEDULING_POLICY`).
* Adds configuration environment variable to set a timeout between consuming workflows (`REANA_SCHEDULER_REQUEUE_SLEEP`).
* Adds configuration environment variable to set an API rate limiter (`REANA_RATELIMIT_AUTHENTICATED_USER`, `REANA_RATELIMIT_GUEST_USER`).
* Adds new `info` endpoint allowing to retrieve information about cluster capabilities such as available workspaces.
* Changes workflow execution consumer to receive only one message at a time.
* Changes to PostgreSQL 12.8.

## 0.7.6 (2021-07-05)

* Changes internal dependencies.

## 0.7.5 (2021-04-28)

* Adds support for listing files using glob patterns.
* Adds support for glob patterns and directory downloads, packaging the content into a zip file.

## 0.7.4 (2021-03-17)

* Adds configuration to set a timeout between `reana_ready` checks. (`REANA_SCHEDULER_SECONDS_TO_WAIT_FOR_REANA_READY`)
* Fixes start workflow endpoint to work with unspecified `operational_options` parameter
* Fixes workflow scheduling bug in which failed worfklows would count as running, reaching `REANA_MAX_CONCURRENT_BATCH_WORKFLOWS` and therefore, blocking the `job-submission` queue.

## 0.7.3 (2021-02-03)

* Adds optional email confirmation step after users sign up.
* Changes email notifications with enriched instructions on how to grant user tokens.

## 0.7.2 (2020-11-24)

* Changes rate limiting defaults to allow up to 20 connections per second.
* Fixes minor code warnings.

## 0.7.1 (2020-11-10)

* Fixes REANA \<-> GitLab synchronisation for projects having additional external webhooks.
* Fixes restarting of Yadage and CWL workflows.
* Fixes conflicting `kombu` installation requirements by requiring Celery version 4.
* Changes `/api/you` endpoint to include REANA server version information.

## 0.7.0 (2020-10-20)

* Adds new endpoint to request user tokens.
* Adds email notifications on relevant events such as user token granted/revoked.
* Adds new templating system for notification email bodies.
* Adds possibility to query logs for a single workflow step.
* Adds endpoint to retrieve the workflow specification used for the workflow run.
* Adds preview flag to download file endpoint.
* Adds validation of submitted operational options before starting a workflow.
* Adds possibility to upload empty files.
* Adds new block size option to specify the type of units to use for disk size.
* Adds a possibility to upload new workflow definitions before restarting a workflow.
* Adds new command to generate status report for the REANA administrators; useful as a cronjob.
* Adds user token management commands to grant and revoke user tokens.
* Adds support for local user management.
* Adds pinning of all Python dependencies allowing to easily rebuild component images at later times.
* Fixes bug related to rescheduling deleted workflows.
* Changes `REANA_URL` configuration variable to more precise `REANA_HOSTNAME`.
* Changes workflow list endpoint response payload to include workflow progress information.
* Changes import/export commands with respect to new user model fields.
* Changes submodule installation in editable mode for live code updates for developers.
* Changes pre-requisites to Invenio-Accounts 1.3.0 to support REST API.
* Changes `/api/me` to `/api/you` endpoint due to conflict with Invenio-Accounts.
* Changes base image to use Python 3.8.
* Changes code formatting to respect `black` coding style.
* Changes documentation to single-page layout.

## 0.6.1 (2020-05-25)

* Upgrades REANA-Commons package using latest Kubernetes Python client version.
* Pins Flask and Invenio dependencies to fix REANA 0.6 installation troubles.

## 0.6.0 (2019-12-20)

* Fixes bug with big file uploads by using data streaming.
* Adds user login endpoints using OAuth, currently configured to work with CERN
  SSO but extensible to use other OAuth providers such as GitHub, more in [Invenio-OAuthClient](https://invenio-oauthclient.readthedocs.io/en/latest/).
* Adds endpoints to integrate with GitLab (for retrieving user projects and creating/deleting webhooks).
* Adds new endpoint `/me` to retrieve user information.
* Improves security by allowing requests only with `REANA_URL` in the host header, avoiding host header injection attacks.
* Initialisation logs moved from `stdout` to `/var/log/reana-server-init-output.log`.

## 0.5.0 (2019-04-23)

* Adds new endpoint to compare two workflows. The output is a `git` like
  diff which can be configured to show differences at metadata level,
  workspace level or both.
* Adds new endpoint to retrieve workflow parameters.
* Adds new endpoint to query the disk usage of a given workspace.
* Adds new endpoints to delete and move files whithin the workspace.
* Adds new endpoints to open and close interactive sessions inside the
  workspace.
* Workflow start does not send start requests to REANA Workflow Controller
  straight away, instead it will decide whether REANA can execute it or queue
  it depending on a set of conditions, currently it depends on the number of
  running jobs in the cluster.
* Adds new administrator command to export and import all REANA users.

## 0.4.0 (2018-11-06)

* Improves REST API documentation rendering.
* Enhances test suite and increases code coverage.
* Changes license to MIT.

## 0.3.1 (2018-09-07)

* Harmonises date and time outputs amongst various REST API endpoints.
* Pins REANA-Commons, REANA-DB and Bravado dependencies.

## 0.3.0 (2018-08-10)

* Adds support of Serial workflows.
* Adds API protection with API tokens.

## 0.2.0 (2018-04-19)

* Adds support of Common Workflow Language workflows.
* Adds support of specifying workflow names in REST API requests.
* Improves error messages and information.

## 0.1.0 (2018-01-30)

* Initial public release.
