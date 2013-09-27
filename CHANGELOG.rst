Changelog
=========

0.2.2
-----

- Fix another one of these that we missed. `916ca7582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916ca75821944d564bcfd5ccc4ded5d200cf057c>`_
- Handle impossibly unlikely datanommer events. `760d9f3b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/760d9f3b692dc1af1ba86d310e61eec621fc51bf>`_
- Only return meetbot links when the meeting is actually over. `9bb73693c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bb73693c7005952860f09fda37288762c3fab7f>`_
- Merge pull request #36 from fedora-infra/feature/wat `605950b3d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/605950b3d8f7f3bf941c36de18015c872a572fbb>`_
- Merge pull request #37 from fedora-infra/feature/no-link-at-start `98ab1adac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98ab1adac0318c57a21791f9517554ec936d0094>`_
- Nuancier stuff. `31a309ca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31a309ca9b57b1ac64bd66e9c37c232def66a2a8>`_
- Merge pull request #40 from fedora-infra/feature/nuancier `52381965d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52381965db4f8637974fde6eb788826ac3f3307e>`_

0.2.1
-----

- Bugfix to ansible relative playbook.  You can run not-checked-in playbooks, btw. `46c82a191 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/46c82a191db5d5e974fdf3ed55645ccae7ce1b0c>`_
- Support rank.advance messages from the badges world. `6f757311f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f757311f2dec5f449f391a852fb3c9aa5b9a167>`_
- Add a test showing that this never worked. `ddcaf59c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddcaf59c046d54ecea680e1613ff861e0928d881>`_
- Fix the ansible relative playbook stuff to make sense and match the test. `5a5541783 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a55417836a6efa3037fb208abd43f66b6c47714>`_
- [scm] fix subtitle for older messages without username specified `ad5e2c7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad5e2c7c2ecb62ce8496cb8af7fe94e78e4aff2d>`_
- Merge branch 'develop' into feature/scm-old-message-bugfix `9f41909b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f41909b91d16a236061b5d326086e9e611680c2>`_
- Merge branch 'develop' into feature/ansible-relative-playbook-bugfix `946ca3bab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/946ca3bab2298c853ef62db8edf45ecf82fabdd5>`_
- Merge branch 'develop' into feature/badges-rank `66d0156e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66d0156e9e5a3108e158a42fbcdfa1a8bda845d3>`_
- Catch up to the latest from the develop branch. `b3619e38a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b3619e38a19f6ed06fa0cecef6ab4bb7a3bddf28>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into feature/scm-old-message-bugfix `6aad75e8c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6aad75e8c871bd96459c5d257d1a293feee1006a>`_
- Add test suite to cover older SCM messages without username specified `8c01e50eb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c01e50eb0bbcddb0d54d1034fed616162d41b1c>`_
- Merge pull request #34 from fedora-infra/feature/scm-old-message-bugfix `a2f793b62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a2f793b62567c4805dff9c9a90e35bb219e7b9bf>`_
- Merge pull request #28 from fedora-infra/feature/ansible-relative-playbook-bugfix `045742bb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/045742bb2e1cdcb5bd216f1344281265270fa481>`_
- Check the contents in _get_user. `32b6ce7ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32b6ce7ab95a3ce5a45bf697e05227a78d432a87>`_
- Merge pull request #32 from fedora-infra/feature/badges-rank `77a03320c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77a03320c2cf1e503539f2de1ad4bc1e282290c2>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `ddca35716 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddca35716872884d8e6973ce398b4f27edf333dd>`_

0.2.0
-----

- Remove unneeded methods. `7cfb39e74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cfb39e7427e70e2cafd2d6e822cccc5110b9fbd>`_
- Use the badge art as the icon, and the user avatar as the secondary. `c1464952b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c1464952b2a131642e45bb4e5f4f099aa29daa21>`_
- Merge pull request #30 from fedora-infra/feature/badge-icons `e610ed014 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e610ed014b739cffd225ab1585d2efe518dfa1e8>`_
- Follow in the footsteps of fedora-infra/fedmsg#173. `26cbcaab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/26cbcaab29f100183e3bc0e1f862abf4b7acadb4>`_
- Handle new git.receive message bodies if they're available. `f18aebe1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f18aebe1f5c3809b4b6259feb8a2f16f17d70d7c>`_
- More pythonic! `022e3c27d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/022e3c27dd3bab327ff84ef4b2ddfcead319b6d1>`_
- Merge pull request #31 from fedora-infra/feature/githook-abspath `610dc7bc0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/610dc7bc0e520d91e78e3c1668011ae152eb106a>`_
- Merge pull request #35 from fedora-infra/feature/idempotency-following-suit `1928d92b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1928d92b0f1dd6a54b1352bc6abee88020a5b257>`_
- Somehow this got left out of one of the merges. `bff70ecee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bff70ecee6991ba8752b739def768e51f3e55c18>`_

0.1.9
-----

- @laarmen asked in #fedora-apps if we could invert the msg2emails dict to make things easier for email-centric debian infrastructure. `53971f006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53971f006a6bcec69ce2d89825a0929724694b24>`_
- Merge pull request #25 from fedora-infra/feature/invert-msg2emails `83b2d3388 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83b2d33885f4758f5a7f5a931f5d718a8b27876e>`_
- Try to preserve some of that memory. `af74d218d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af74d218d3df49ee381b8e0495e016e6b8c4af09>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `6cf9bd865 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6cf9bd865ee62ba15c28e225094932cffbb15aad>`_
- Update the link url for badges. `548b749c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/548b749c2093bbb16f2becb71e531fe1eea01e17>`_
- Revert "Update the link url for badges." `1fbef4ab6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fbef4ab645004926194c9c3a18e4a06433815d1>`_
- AnsibleProcessor with tests. `c5a380b7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c5a380b7f474c7a1ea2576c77d097cd26cee275f>`_
- Be more careful when constructing relative_playbook. `ca33e4b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca33e4b5ac4e5bce9167c96bd5e8e8b4ad653a53>`_
- Merge branch 'feature/ansible' into develop `88d07f247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/88d07f247c809d7794983d2777ad5aba32348d93>`_

0.1.8
-----

- Cover more cases when determining the tagger icon.  Fixes #21. `2a3db0417 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3db04176ab21a14dc8a6cab71fef9889cc7d44>`_
- Correct/nicer link for badges. `f9ec367ac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9ec367ac2283fa8b23468d63c82c3a846afb3c3>`_
- Merge pull request #22 from fedora-infra/feature/tagger-icon `4fbec04b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4fbec04b18ab2b68c66684d6ecbd5ea2f60a6937>`_
- Merge pull request #23 from fedora-infra/feature/username-for-badge-links `76a168cd4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/76a168cd40108ff06ce44898e21fef77a75ff993>`_
- [mediawiki] Nuke a '.' for consistency in subtitles. `3e361c43d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e361c43de1d6fa6682a8cf1c77c60a628ae3a44>`_
- Merge pull request #24 from fedora-infra/feature/string-consistency `2809dc57d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2809dc57d3b8a7a13081b5d0df8158ec3623613d>`_
- Remove a period that was missed in a previous commit. `64888923d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64888923d8f0459846daf6dbe66e9b9c22fbd76a>`_
- Cache fas for irc msg2usernames and friends. `85b40d6fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85b40d6fcbf0393ea459e79871f9dd9d9552f487>`_
- Mock out the fas cache during tests. `3d46f885c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3d46f885ced8bc1efdbb46a00b4ae0fef5a0e094>`_
- Random cleanups pointed out by @lmacken. `bda4c8c71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bda4c8c7190662c045a9591762a88756aadb722b>`_
- Be more careful with that default socket timeout. `6df24e52e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6df24e52ec45d1d8f4912df8efa076e1ee5e3483>`_
- Merge branch 'feature/fas-cache' into develop `bfa3fa45d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bfa3fa45d009639055383a165c038430f2d7724f>`_
- @relrod says people > persons `3d043f4de <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3d043f4de63e5d469fc9936f0087575554d49a1e>`_

0.1.7
-----

- Added failing test for badge messages. `4a5826704 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a5826704953f01a221c62fb877ca5a47806d673>`_
- Update tests with a more current message example. `b29097948 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b29097948f39d9aa2efd9ee6b889c3f1adca1a68>`_
- Add the processor for badges messages. `a6259e308 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6259e308ad254e2df277b1fa97e611361f49ac9>`_
- Merge pull request #20 from fedora-infra/feature/badges `fade3fdda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fade3fdda827f1d5722925cd0efad2e3832792c9>`_

0.1.6
-----

- Don't declare tickets open or closed unless the status has actually changed. `9e7b13a64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e7b13a64dbc285ef68249dd7283b87c2df54000>`_
- Make PlanetProcessor.__name__ match the actual message topic `2140e1154 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2140e1154f555bf2e3eb2e193d36d5154bbc0dfe>`_
- Reorganize fas shim to: `3512466f8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3512466f838c6761c66312a6ab5e9454079612db>`_
- Mailman3 processor and test. `aa71d2484 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa71d2484f665493aefff0e99cb1f1dba55c946f>`_
- PEP8 and corrections. `48a2c6183 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/48a2c61832f0fe888706fd4677b941744abdd0d2>`_
- The "references" header actually specifies whether or not it is a reply. `ca575bdd9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca575bdd9588ec94b771b3e8f9af2dbdfb2bdec4>`_
- And... references can be None. `5ff1ea136 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ff1ea136e66dd586c7456a70ea48326dcdd53f3>`_
- Another test for mailman. `2762640f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2762640f26ea286114ef1ca63bbfcbc7eab87266>`_
- Emit a warning and don't TB when handling an invalid mailman3 message. `b37d76d43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b37d76d43d64e0f1ba9eb2a79f27b7eabf124e9e>`_
- Check both "references" and "in-reply-to" headers when determining mailman3 subtitle. `8b01fb543 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b01fb543d385317abdf06dbca6cd3f82045dad7>`_
- Modify test to handle both cases. `aaca846d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aaca846d0cb91d99901188f917e191bbc0bd2c88>`_
- Handle that dichotomy in the mailman .objects method, too. `694b4a1c6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/694b4a1c647285805745e7b9ba751eb99f3189ce>`_
- Merge pull request #18 from fedora-infra/feature/mailman3 `2d672aafb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d672aafb6a9a98b792e5c6689c88f979b2d8431>`_

0.1.5
-----

- Point all compose links at dl.fp.o. `77056aad2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77056aad208cdd32e4943547dca3333d8738f826>`_
- Add a local BaseProcessor that produces fedora-specific emails and gravatars for messages. `25816d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25816d49c1fffaaf0b8ad86513dc7f49ab5e49b6>`_
- Add an example email and avatar test. `2d52e4559 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d52e4559a6f2cc28899693abe98c01388cff0f5>`_
- Leave libravatar optional for now. `ce07184ac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce07184ac365aebc5738f4ee63199654cec1d666>`_
- Merge pull request #13 from fedora-infra/feature/dl `1a7144ffa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7144ffae244a1f35e66e52a084d0f4581560d3>`_
- declare that encoding. `1e0c753ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e0c753add4aa4d6c8f49f60db79172f7dd9831b>`_
- Merge pull request #16 from fedora-infra/feature/avatars-and-emails `48d8b81cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/48d8b81cf07f5aac047b00bc5dd67f7e3286ceae>`_
- Initial test for trac messages. `75626ce7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/75626ce7f7f5b902ed36f26c592ae54407e23f8d>`_
- PEP8 `611e55925 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/611e559253449993a0a919903b95837aec1587d7>`_
- Correct a test topic. `e1d2b0cd5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1d2b0cd5c23bdabc023ef9fc6e8662ab5226910>`_
- Add some fields we are going to need. `380cfd7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380cfd7c2f6be76e137e5e6bec515a7251543066>`_
- Trac processor implementation. `d858857b8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d858857b8094fd1da62bbbe0000d050aee0de141>`_
- Use appropriate base class. `af2183e0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af2183e0d0b5b8eac3f06815454685e4845a1b7f>`_
- Merge pull request #17 from fedora-infra/feature/trac `3e46a0c91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e46a0c9112b48b1eb3b2f08794cb1677ee23ef5>`_

0.1.4
-----

- Move tagger tests out into their own submodule. `ff128fe28 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff128fe287edcadc1e6ca432df714968ee873e64>`_
- Whoops.  Forgot to include this file. `49bb7e9f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49bb7e9f49794972911b7c84f34660409dc75019>`_
- Test old and new tagger messages both. `2286df1d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2286df1d9ed93461772e5dd3942188b663394290>`_
- Compatibility with old and new tagger messages. `a2ee0dd3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a2ee0dd3b7ff78ee4e4035520c11347ee1781367>`_
- Add anonymous field to new messages. `9a4f37c76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a4f37c766504eebe9138e4d1114a77da1925ef1>`_
- Add test for tagger rating changes. `5cb6f58bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb6f58bf0436549b7db1ce379f70d4ff2ef29e5>`_
- Fix syntax errors. `5bcc4a0d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bcc4a0d58d70dc58bb8928e2405d84d00ac3205>`_
- Handle fedoratagger rating updates. `daecc80b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/daecc80b38a75c3e12a5b7b1392ee2e1fb20b381>`_
- Merge branch 'feature/tagger' into develop `8c6d7c0cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c6d7c0cd0928477945c92917a574fcb6735a32d>`_

0.1.3
-----

- Make sure we can handle a None for the user in koji messages. `3277e6016 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3277e60160665c0158e89afd925812c38b4dc92a>`_
- Make messages make a little more sense when there is no owner of a koji build. `2311934ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2311934ec8ebc7901fdc45172f7b2967c0d38632>`_
- Typofix. `bed16f607 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bed16f607163af616b2bebbbe8603211076e0694>`_
- Be more careful with old pkgdb2branch messages from datanommer. `307a1cd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/307a1cd5fe29e8c4d58e1686c4ab533e3562a005>`_

0.1.2
-----

- For dgilmore, remove the "for public consumption" clause. `e6addbe3f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6addbe3fb3c8ca1eaefa98bb054b266b4ad4095>`_
- Rename __doc__ to .doc for the topics-to-doc script. `34c169793 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34c169793a573a750a39cd8faef538d2f57cff25>`_
- Docstrings for askbot tests. `95967c2fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/95967c2fcf50218e44c7679bec62b18b5a50807f>`_
- Correct factual error. `6dcead744 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6dcead744ab7259769e192c942ab53063d1ae1a6>`_
- Koji docstrings. `da06d7f2c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/da06d7f2cc1e82f751110e0548707d5703a25428>`_
- Compose docstrings. `e7e7b08ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7e7b08ea8f30fcaee0e45a9839f2a520e829ff4>`_
- Pkgdb docstrings. `2cb033f2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cb033f2b273ea5672b91f26d19a164235c3bf3d>`_
- Planet docstrings. `c382b4846 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c382b4846e7b4e54d7addc4df54ab5a0c1fe5484>`_
- s/OldStyle/Legacy/g `bf9ec9c4b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bf9ec9c4b332e01972beec617219681e747df8b3>`_
- FAS docstrings. `24e78b272 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24e78b272e3f3b35b31d9783b8ebb39e194ca0a4>`_
- Bodhi docstrings. `f7339d401 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f7339d401977644b8c638d42cd8bb653889bb392>`_
- Fix old test that I missed a long time ago. `92e863c85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e863c855b65a1e004335053060a32849c0ed9f>`_
- Meetbot docstrings. `1752eca88 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1752eca88924e96739a76437882cf150edda9039>`_
- Fedora Tagger docstrings. `e29fcdc9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e29fcdc9f6dc4533aa45b67260bb51b6b79d4d10>`_
- Wiki docstrings. `341aad86d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/341aad86dfc1fe79cf8072408d609051336b7225>`_
- pkgdb2branch messages. `4651e6f16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4651e6f163b54fd9eb302f4efc3d6db2aff14b35>`_
- SCM messages. `226b7e0fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/226b7e0fd182b1959234387294bd30b04ec7f9f9>`_
- Merge pull request #12 from fedora-infra/feature/docstrings-for-tests `a24c54cd9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a24c54cd9631816c838363f7cb7d16b031beaab7>`_

0.1.1
-----

- Use the non-https fedorahosted cgit url until infra#3672 is fixed. `916fb9973 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916fb99733870ced83d1620d144eca8990f4f05c>`_
- Give up on askbot deep linking. `f63baad50 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f63baad500eb49a41f9d6d070a9a99b1a99ad58c>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `732e0133f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/732e0133f324e59ea8d754922d3482a63822a82e>`_
- Better debug of unhandled messages. `42527d43d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42527d43da061e8658715bcabdc0d71a1a22b583>`_
- Handle messages on the buildsys.package.list.change topic. `202fe1ec7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/202fe1ec7aabcf865915690b026f19a7a70581da>`_
- Merge pull request #5 from fedora-infra/feature/better-debug `d2c5aeb5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2c5aeb5fa5f169bcacd0a5487ddd93d48730aab>`_
- Merge pull request #6 from fedora-infra/feature/the-missing-link `f910853ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f910853ad19be9670f4037c077d6265fdc0cae59>`_
- The planet currently doesn't support https `08e667995 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08e66799536b67225e8dc9995a06327865b20ffe>`_
- Handle topic changes from meetbot. `4fff9631d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4fff9631ddf24884cd9aa4ea496d651ffe4e5a6e>`_
- Handle links from koji package list changes. `b89e7269d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b89e7269de1fbf094013d809c1b4f8bacf949163>`_
- Satndardize absence of "object" prefix. `2f96c6c4a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f96c6c4a4586d96cced71e04587a66a10c85e9f>`_
- Move compose tests out of the big test file (for organization's sake) `252445802 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25244580241cb465c9a8d8d3c2a66e80b31d7319>`_
- Add message bodies to compose tests that are already being sent in production. `4bebe3a73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bebe3a738a04473d9e7a4b7516518e73e9a91fd>`_
- Use actual branch name for "branched" compose messages. `43476f661 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43476f661f3f51b2bca9eb4cc1e558990d12d1b3>`_
- Duplicate compose tests into legacy and newschool (over the addition of an "arch" field) `f6605fa0c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6605fa0c726ef34a7a1f946f1da82526682f311>`_
- Secondary arch compose tests. `773578b38 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/773578b38f54249e5b6ddba806b5bd8c231291d6>`_
- Tweaks to primary compose tests. `49b26d5b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49b26d5b9561ed07ace4bae1c461f6d56c5a92a9>`_
- Straighten compose processor out to meet the new tests. `287fc165e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/287fc165e8bad3a82883a66ed9cf6a7ca83c686a>`_
- Merge pull request #7 from fedora-infra/feature/standardize-object-prefix `0b9cb2b7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b9cb2b7fd7b25de6cac33d1c8fba425461e9765>`_
- Merge pull request #10 from fedora-infra/feature/secondary-arch-compose `12b7f2ae2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12b7f2ae25ad8739dba2a0110f938234c9008e16>`_
- Merge pull request #9 from fedora-infra/feature/meetbot-topic-changes `166190804 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/166190804724bd41230408951e516cf61e67e077>`_
- Merge pull request #8 from fedora-infra/feature/koji-list-change-links `85e39afc0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85e39afc01a19b1cbc018f1d8c8b4bc6490219ce>`_

0.1.0
-----

- Use the bodhi 'agent' instead of the update submitter (fixes #113) `c5bceac66 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c5bceac669782e4ffe70a7ec179eef318409cc1d>`_
- Add support for the new msg['agent'] to the bodhi unit tests. `fda949837 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fda94983777358067e3bd314cb2f49b084398442>`_
- Set KojiProcessor.__name__ to 'buildsys' instead of 'koji'. `ecff43baf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ecff43baff22c275ff8e6c7862d4795f80eaadfd>`_
- Include the "tagger" in buildsys messages. `1e89b2cd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e89b2cd7a28d91b5dfcfbaab47d837e578c1cd0>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `385825ae8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/385825ae85eb60114e141039e2c4c10064c2b78e>`_
- Set KojiProcessor.__name__ to 'buildsys' instead of 'koji'. `d1162492e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d1162492e5619cfeffb96af186f33fb4959d04ad>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `de19b5d6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de19b5d6b29cf5cefdb2d25e6559b7d61350f03a>`_
- First round of tests for askbot plugin. `45ecb9b60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45ecb9b609742c8a6ba3cb2477b852975e1cab9d>`_
- All askbot handlers except for subtitle. `1d54042f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1d54042f2ade37f77623b94e9a5f9a7ad6789ca0>`_
- Some subtitle for post edits. `7c82aff2d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c82aff2d9800afd91564935824b7b718d68b57a>`_
- Fixes to one deletion test. `989ffa582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/989ffa582c29de74b59c7d18435ee77c0f03b7bf>`_
- Last of the subtitle code for askbot. `e0a96d96c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0a96d96cefc1b6fcb9d22f9aa068228bcb2f0e1>`_
- pep8 `746984328 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74698432813a723f079d6df656db1672e9b68c6b>`_
- Little tweaks. `1e722d1cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e722d1cb4fc9e16503ad4789a7334872a1c8fc5>`_
- s/pkgdb/askbot/ `6f1778a9c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f1778a9c3c7921f1dcf930d7474504c88947976>`_
- Move some tmpl.format calls out a level of nesting for simplicity's sake. `4860bc08b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4860bc08bd5540791cd23f011238d39c545b3813>`_
- Merge branch 'feature/askbot' into develop `79a455bf4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79a455bf476006f56ed0e87b8322ff1a4e256382>`_
- Handle old-style scm messages. `0af3e1981 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0af3e19818edd95d1ef0ab951b29cf63552daf87>`_
- For koji, use http links, not https. `16325cd5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16325cd5a6d48a1db72b1321ca6902bf09d4f2db>`_
- Use https for compose messages, not http. `1dd78964b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1dd78964b245e530c611b898103f99f504e98762>`_
- Merge pull request #2 from fedora-infra/feature/http-not-https `5f2540646 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f2540646cbeb2857e02cf092b7b956c4c61e384>`_
- Merge pull request #3 from fedora-infra/feature/https-not-http `05d39c33f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d39c33f72d57c40c19159fa14852be364a36dd>`_
- Fix up koji tests after the https shuffle. `10e3c6268 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10e3c626893f4e113981bc62d59ebbb6c1cceb9c>`_

0.0.9
-----

- STATE 1 is "closed" `9d7bb2275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d7bb227569ae2dac678726306bb74a52a312569>`_
- Much better.  Use the correct enums from koji. `2466d2b9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2466d2b9ffea0da446bee238046c0236a745efce>`_
- Handle new and old style fas messages. `b4962173e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4962173ec0b07a02e59715a5d80342e96833f3c>`_
- Handle usernames and links in koji messages. `4ee46b0f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ee46b0f73b58605e1af0f6f55459ebe507184ae>`_

0.0.8
-----

- Planet Processor. `f4ba3a0b8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4ba3a0b871716bc800cfbf24a505e62404698e8>`_
- Stubs for buildsys.tag. `0a6c6e1d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a6c6e1d69db0f8ca9e4f77f28b3a07682c1f92b>`_
- Handle some build state changes. `02c612e54 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02c612e540556a2a1c9fa866a4cc0e4e16c4dbca>`_
- buildsys untag and repo.ini messages. `b4db03029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4db0302961fe3139b6181664673cd6db9e9bfe8>`_
- One last koji message type. `18eef2a3e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/18eef2a3eefeca6afe4c05f0b92c210fd727a068>`_

0.0.7
-----

- Updates for git topics. `aaca74704 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aaca74704b9470a846e1bd25ea88b3ba661efd80>`_
- 0.0.6 `5ce1a8027 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce1a8027ce0fe4d139d8d73fd9abe6248445095>`_
- Fix to git.lookaside messages. `a1abbc0ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1abbc0ab186eb0560e8924dd85298c931185b37>`_

0.0.5
-----

- Support for new git/scm messages. `de2bc9570 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de2bc9570b08a7db0f7a456a7bb2cb61668e75bb>`_
- Same for lookaside messages. `751b86b3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/751b86b3bb9e81bf5812d5a514c4e765af14ea5b>`_

0.0.4
-----

- Added a config for tests. `a0e9db882 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a0e9db8826f5292c10c1612ceeb35a8b534a404a>`_
- Change namespace to fix tests. `c509d0787 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c509d078773c4b6bb94c9b81c3b187c964bc4560>`_
- First pkgdb messages. `11e50b58b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11e50b58bc8c8274aebb39d9d710ddb1db70cdce>`_
- TODO list. `bb805e545 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb805e545ae81995840d8cc27f383e9a5f3c259a>`_
- pkgdb.owner.update. `126579c3f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/126579c3f69d9dfb099387ccf315b22d8ffc4c47>`_
- pkgdb.acl.request.toggle. `4ca441a9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca441a9dc8b61ce3f965aa795d658fc33e7b29d>`_
- grammar `a460e9ec3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a460e9ec3d8f8404005cfb93b449b19a0f7daced>`_
- pkgdb.package.retire. `aae5bb1fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae5bb1fcc0bff32690bed37c36cc0f8d70ba1aa>`_
- todo update. `b665aa428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b665aa428e9098eb267c7c6b370295f1227b4eff>`_
- pkgdb.acl.user.remove. `93372562a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93372562a25a6d6755362ebe40678d2cbebf6177>`_
- pkgdb.package.new. `112ca191f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/112ca191ff34e2f400c1677bcc168210be58c791>`_
- pkgdb.package.update. `41357a555 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41357a55596ecd40c926438205e31b6adf4eafb6>`_
- pkgdb.branch.clone. `5402557bc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5402557bc3382c47fb9b384f749d06da5d9d292a>`_

0.0.3
-----

- s/fedmsg.text/fedmsg.meta/g `eb05cfe8a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb05cfe8a0499323f1958a2f406e36d65a3edb8e>`_
