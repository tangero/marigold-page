---
slug: "ec-pch"
url: "/mobilnisite/slovnik/ec-pch/"
type: "slovnik"
title: "EC-PCH – Extended Coverage Paging Channel"
date: 2025-01-01
abbr: "EC-PCH"
fullName: "Extended Coverage Paging Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ec-pch/"
summary: "Kanál GSM/EDGE navržený ke zlepšení pokrytí pagingu pro IoT a MTC zařízení v náročných rádiových podmínkách. Využívá opakované přenosy a pokročilé kódování k dosažení zařízení hluboko v budovách nebo"
---

EC-PCH je kanál GSM/EDGE, který využívá opakované přenosy a pokročilé kódování ke zlepšení pokrytí pagingu pro IoT a MTC zařízení v náročných rádiových podmínkách, jako jsou hluboko v budovách nebo venkovské lokality.

## Popis

Extended Coverage Paging Channel (EC-PCH) je logický kanál v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)) specifikovaný v 3GPP TS 44.060. Je klíčovou součástí technologie Extended Coverage GSM (EC-GSM), která je součástí sady funkcí Cellular Internet of Things (CIoT). EC-PCH je zodpovědný za doručování pagingových zpráv ze sítě k uživatelskému zařízení (UE), konkrétně cílených na zařízení pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)), která vyžadují rozšířené pokrytí přesahující standardní možnosti GSM. Jeho primární funkcí je upozornit zařízení na příchozí hovor nebo datovou relaci, což je kritický proces pro komunikaci iniciovanou sítí, zejména pro IoT aplikace, kde mohou být zařízení umístěna ve sklepích, hluboko v budovách nebo v odlehlých zemědělských lokalitách s výrazným útlumem signálu.

Architektonicky EC-PCH funguje v rámci rámcové struktury GSM, ale využívá specializované techniky fyzické vrstvy k dosažení svých cílů rozšíření pokrytí. Je mapován na prostředky Physical Random Access Channel (PRACH) vyhrazeným způsobem pro provoz EC-GSM. Kanál využívá tzv. blind přenosy na fyzické vrstvě, což znamená, že se nespoléhá na předchozí odhad kanálu nebo zpětnou vazbu od zařízení, což je klíčové pro dosažení zařízení s extrémně nízkou úrovní signálu. Přenosové schéma zahrnuje odesílání stejné pagingové zprávy vícekrát napříč různými rádiovými bloky a rámy, což je metoda známá jako opakovací kódování. Tato časová diverzita umožňuje přijímacímu zařízení použít techniky kombinování, jako je Chase Combining nebo přírůstková redundance, k akumulaci energie a zvýšení pravděpodobnosti dekódování pagingové zprávy i přes velmi nízký poměr signál-šum (SNR).

Provoz EC-PCH je těsně integrován s pokrytími třídami systému EC-GSM. Zařízení jsou kategorizována do různých pokrytí tříd na základě jejich odhadované ztráty na trase k základnové stanici. Síť používá toto klasifikování k určení odpovídajícího počtu opakování pro pagingové přenosy na EC-PCH. Zařízení v horší pokrytí třídě (např. Coverage Class 3 nebo 4) bude pagingováno s použitím vyššího počtu opakovaných bloků, což výrazně zvyšuje pravděpodobnost úspěšného příjmu. Kanál podporuje jak individuální paging (adresování jednotlivého International Mobile Subscriber Identity - [IMSI](/mobilnisite/slovnik/imsi/)), tak skupinový paging (adresování skupiny zařízení), což je efektivní pro IoT scénáře, kde mnoho zařízení může potřebovat být upozorněno současně pro aktualizace softwaru nebo skupinové příkazy. EC-PCH spolupracuje s Extended Coverage Broadcast Control Channel ([EC-BCCH](/mobilnisite/slovnik/ec-bcch/)) a Extended Coverage Synchronization Channel ([EC-SCH](/mobilnisite/slovnik/ec-sch/)) za účelem poskytnutí kompletních systémových informací a synchronizace potřebných pro zařízení k řádnému monitorování a dekódování pagingových zpráv.

## K čemu slouží

EC-PCH byl vytvořen, aby řešil základní výzvu poskytování spolehlivé konektivity pro zařízení Internetu věcí (IoT) a komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) umístěná v lokalitách se špatnou intenzitou rádiového signálu. Tradiční pagingové kanály GSM byly navrženy pro služby hlasu a dat orientované na člověka, za předpokladu, že zařízení jsou obecně v rozumných oblastech pokrytí. Nicméně IoT případy použití, jako jsou chytré měřiče instalované v podzemních sklepích, zemědělské senzory v odlehlých polích nebo sledovací zařízení uvnitř přepravních kontejnerů, často zažívají ztráty na trase o 20 dB a více přesahující standardní limity návrhu GSM. To činilo komunikaci iniciovanou sítí (kdy síť potřebuje kontaktovat zařízení) nespolehlivou nebo nemožnou, což omezovalo použitelnost GSM sítí pro masivní nasazení IoT.

Motivace pro EC-PCH vycházela z potřeby průmyslu po nízkonákladovém řešení IoT pro široké oblasti, které by mohlo využít stávající, všudypřítomnou infrastrukturu GSM. 3GPP prostřednictvím práce na Cellular IoT v Release 13 usilovalo o vylepšení GSM, aby mohlo konkurovat necelulárním LPWAN technologiím, jako jsou LoRa a Sigfox. Základním požadavkem bylo dosažení maximální ztráty vazby ([MCL](/mobilnisite/slovnik/mcl/)) až 164 dB ve srovnání s přibližně 144 dB u starších verzí GSM. Pagingový proces je kritickým článkem tohoto řetězce; pokud zařízení nelze pagingovat, síť mu nemůže doručit data. EC-PCH to řeší zavedením robustních, opakovaných přenosů, které mohou být úspěšně dekódovány i při velmi nízkých úrovních SNR.

Před EC-GSM byla řešení pro dosažení zařízení v extrémních dírách pokrytí ad-hoc nebo zahrnovala proprietární opakování na aplikační vrstvě, která byla neefektivní a nestandardizovaná. EC-PCH poskytuje standardizovanou, síťově řízenou metodu pro paging s rozšířeným pokrytím. Zajišťuje zpětnou kompatibilitu a koexistenci s provozem starších verzí GSM tím, že funguje na vyhrazených časových slotech a používá specifické modulace a kódovací schémata. To umožňuje mobilním operátorům upgradovat své sítě pro podporu služeb CIoT bez narušení stávajících hlasových a datových zákazníků, což umožňuje hladký přechod k podpoře masivní komunikace typu stroj-stroj.

## Klíčové vlastnosti

- Využívá blind přenosy s opakovacím kódováním napříč více rádiovými bloky pro zvýšení pokrytí
- Podporuje více pokrytí tříd, což síti umožňuje přizpůsobit počet opakování na základě ztráty na trase zařízení
- Umožňuje jak individuální paging (podle IMSI), tak skupinový paging pro efektivní správu IoT zařízení
- Funguje na vyhrazených fyzických prostředcích (PRACH) v rámci rámcové struktury GSM pro EC-GSM
- Navržen pro maximální ztrátu vazby (MCL) až 164 dB, což výrazně překračuje možnosti starších verzí GSM
- Integruje se s kanály systémových informací (EC-BCCH) a synchronizace (EC-SCH) systému EC-GSM pro kompletní přístup k systému

## Související pojmy

- [EC-RACH – Extended Coverage Random Access Channel](/mobilnisite/slovnik/ec-rach/)
- [EC-SCH – Extended Coverage Synchronization Channel](/mobilnisite/slovnik/ec-sch/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EC-PCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec-pch/)
