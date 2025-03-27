---
categories:
- Blockchain
- Krypto
- Energetika
excerpt: null
layout: post
summary_points:
- Blockchain může odstranit prostředníky v energetice a snížit ceny elektřiny.
- Implementace blockchainu v energetice vyžaduje překonání právních a technických
  překážek.
- Uživatelé by museli aktivně spravovat nákup elektřiny, což přináší rizika.
- Motivace firem pro blockchain v energetice je často spojena s udržením části provizí.
title: Blockchain v energetice
---

Výzva, ať se  [lidé zkusí zamyslet nad tím, jak by mohl být blockchain přínosný pro republiku](/postavime-republiku-na-blockchainu-kdyz-vas-napadne-jak-dostanete-trezor), se uchytila, pár zajímavých nápadů se objevilo. Zejména na Facebooku mě ale nepříjemně překvapilo počet mektalů. Jasně, že blockchain nepostaví dálnice, jenže my máme milion věcí, co je potřeba řešit a to blblání u lidí jako Martin Jaroš spíš zaráží.

Abych vytáhl příklad, kde může být blockchain technologie zajímavá, tak se můžeme podívat do energetiky.

To je vysloveně podhoubí pro implementaci decentralizované technologie z několika důvodů:

1.  jsou tu peníze, čili je jak odměnit provoz blockchainu
2.  obchodník jako prostředník je opravdu pouze prostředník zajišťující nákup a prodej plus fakturaci, žádnou podstatnou infrastrukturní službu nad tím neposkytuje
3.  obchod je plně digitalizovatelný (vlastně již dnes)

Z toho důvodu se také objevila celá řada pokusů blockchain do energetiky naportovat, nejvíce pak v rámci prodeje energie. Záměr je jednoduchý: člověk si koupí elektřinu prostě tak, že do nějaké utilitky zadá, jakou chce, kolik chce zaplatit a utilitka mu to spáruje a zařídí platbu, přičemž všechno se propíše přes nějaký blockchain.

Všimněte si, že jsem to popsal dosti volnými slovy. To proto, že ďábel je ukrytý v detailu, jak to tak bývá. Tak především ne v každé zemi může výrobce elektřinu také jednoduše prodávat maloobchodně a maloobchodní prodej je něco mírně jiného, už třeba množstvím faktur, výkaznictvím a jistou mírou podpory na infolince. Třeba v Česku se platí zálohy, jejichž výše je dosti přesně stanovená vyhláškami. Jednou za čas (ročně) se provede doúčtování. Z toho by se blockchain (a člověk, co by to do něj pasoval) vobkreslil.

Významem blockchainu v tomto případě má být odstranění prostředníka, obchodníka, který si vezme 10-20% z transakce, tedy o to navýší cenu elektřiny. Většinu jeho rolí může zastat koncový uživatel, část (zejména clearing a účtování) pak blockchain technologie a dodavatel.

Workflow může být zhruba toto:

1.  v aplikaci se podíváte, jakou elektřinu a na jak dlouho si můžete objednat. Aplikace čte nabídky z blockchainu, přičemž právě finanční náklady na zařazení do blockchainu docela brání tomu, aby se ospamovával nesmyslnými nabídkami.
2.  Sami uvážíte, na jak dlouho dopředu si chcete elektřinu koupit a za kolik. Zda na zítra, na týden nebo na měsíc atd. A vyberete si správné nabídky.
3.  Transakce se propíše do blockchainu a ověří, čímž máte vy nakoupeno a dodavatel dostává [token](/ai/tokeny-versus-slova/) pevně svázaný s eurem (čili neřeší kurzovou ztrátu).

**Problémů je pár,**  především moment, kdy si zapomenete elektřinu objednat. Většina systémů to řeší tak, že spadnete do základní dodávky za nějakou přednastavenou cenu.

Druhý moment je psychologický, vy rozhodujete, na jak dlouho kontrahujete elektřinu a za kolik, takže si hrajete na tradera.

Další momenty jsou praktické, zejména napojení na stávající energetickou infrastrukturu. Například Lition fungující v Německu je sice teoreticky blockchainový decentralizovaný projekt, ale formálně jej zprostředkovává obchodník, protože jinak by to právně udělat nešlo. Ve výsledku tady není zřejmé, jaký konkrétní přínos blockchain oproti centrální databázi má, snad s tou výjimkou, že v případě liberalizaci až do úrovně API by bylo možný to jednodušeji skutečně decentralizovat, protože by to na to bylo připravené.

Většině firem, které se do portace blockchainu do energetiky daly, netrvá většinu času ohnutí konceptu blockchainu, ale především prošlapání cest. A nakonec, s ohledem na to, že se snaží vyšoupnout ze hry prostředníka a tím i sebe sama, je problematická jejich motivace. Většinou to hrají na to (Siemens s LO3 Energy), že jejich technologie způsobí dramatické snížení provizních poplatků, ale nějakou část jich ponechá, proto ne všechno z blockchainu v energetice má tendenci být plně veřejné a otevřené. Tichý vendor lock in.

Co zůstává jako otázka? Zda si lidé kvůli hypotetické úspoře 2000 Kč ročně budou chtít hrát s nějakou online nákupní aplikací a neprojebou více na tom, že si zapomenou objednat za levno (a spadnou do drahého odběru) či přešpekulují trh a nakoupí zbytečně draho, když cena půjde dolů (což se nestane ovšem často).