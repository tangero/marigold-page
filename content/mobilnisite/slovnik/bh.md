---
slug: "bh"
url: "/mobilnisite/slovnik/bh/"
type: "slovnik"
title: "BH – Block Header"
date: 2025-01-01
abbr: "BH"
fullName: "Block Header"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bh/"
summary: "Bloková hlavička (BH) je struktura protokolové datové jednotky používaná ve specifikacích 3GPP pro přenos dat, zejména v kontextu služby krátkých zpráv (SMS) a dalších nezávislých protokolů jádra sítě"
---

BH je struktura protokolové datové jednotky používaná ve specifikacích 3GPP k poskytnutí řídicích informací pro segmentaci, znovusestavení a směrování datových bloků.

## Popis

Bloková hlavička (BH) je základní součástí protokolových datových jednotek definovaných v 3GPP TS 43.064, která specifikuje celkový popis služby General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) a Enhanced Data rates for GSM Evolution ([EDGE](/mobilnisite/slovnik/edge/)) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) pro rozhraní Gb. Funguje v rámci vrstvy Base Station System GPRS Protocol ([BSSGP](/mobilnisite/slovnik/bssgp/)), která spravuje tok dat a signalizaci mezi Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)). BH je připojena před uživatelská data nebo signalizační zprávy, aby vytvořila kompletní BSSGP protokolovou datovou jednotku ([PDU](/mobilnisite/slovnik/pdu/)), což síti umožňuje správně zpracovávat a směrovat informace.

Strukturně obsahuje Bloková hlavička několik klíčových polí, která řídí zacházení s následujícím datovým blokem. Mezi klíčové součásti patří Block Type (typ bloku), který identifikuje povahu PDU (např. data nebo signalizace), a Block Length (délka bloku), která určuje celkovou velikost BSSGP PDU. Další pole mohou obsahovat identifikátory pro Network Service Entity ([NSE](/mobilnisite/slovnik/nse/)) a Base Station System Virtual Connection (BVC), které jsou nezbytné pro směrování bloku ke správnému logickému připojení v rámci rozhraní Gb. Hlavička zajišťuje, že každý blok je doručen příslušné zpracovatelské entitě v rámci BSS nebo jádra sítě.

Během provozu, když SGSN potřebuje odeslat paket k mobilní stanici (MS) přes BSC, zabalí tento paket do BSSGP PDU, počínaje Blokovou hlavičkou. BSC využívá informace v BH k rozhodnutí, jak blok zpracovat – například, zda má být přeposlán do konkrétní buňky nebo zda vyžaduje speciální zacházení z hlediska kvality služby (QoS). Stejně tak uplinková data z MS následují opačnou cestu, přičemž BSC před odesláním bloku do SGSN přidá patřičnou BH. Tento mechanismus podporuje různé služby GPRS/EDGE, včetně SMS přes GPRS, tím, že poskytuje standardizovaný způsob řízení komunikace orientované na bloky.

Role Blokové hlavičky je klíčová pro zachování integrity a efektivity přenosu dat přes rozhraní Gb. Umožňuje funkce jako řízení toku díky možnosti sítě spravovat rychlost datových bloků a zpracování chyb díky možnosti identifikace a opětovného přenosu poškozených bloků. Navíc návrh BH podporuje multiplexování více logických připojení přes jediný fyzický spoj, čímž optimalizuje využití prostředků v rádiové přístupové síti. Její konzistentní aplikace napříč vydáními 3GPP zajišťuje zpětnou kompatibilitu a hladký vývoj technologií GERAN.

## K čemu slouží

Bloková hlavička byla zavedena, aby řešila potřebu strukturované a spolehlivé metody přenosu datových bloků v sítích GPRS a EDGE. Před její standardizací rané mobilní datové služby postrádaly jednotný protokol pro nezávislé přenosy zpráv, což vedlo k potenciálním problémům s interoperabilitou mezi síťovým zařízením od různých dodavatelů. BH jako součást vrstvy BSSGP poskytla společný rámec pro zapouzdření uživatelských dat a řídicích informací, umožňující bezproblémovou komunikaci mezi jádrem sítě a rádiovou přístupovou sítí.

Historicky vývoj GPRS vyžadoval paketově přepínaný doplněk k okruhově přepínané síti GSM. To si vyžádalo nové protokoly pro řešení směrování paketů, řízení toku a správy prostředků přes rozhraní Gb spojující SGSN a BSC. Bloková hlavička se objevila jako klíčový prvek této sady protokolů, řešící problém, jak efektivně zabalit a identifikovat datové bloky bez závislosti na specifikách podkladové přenosové sítě. Umožnila oddělení úkolů, kde BH řeší logické směrování a řízení, zatímco nižší vrstvy spravují fyzický přenos.

Vytvoření BH bylo motivováno omezeními dřívějších metod přenosu dat, které byly často těsně svázány s konkrétními přenosy nebo postrádaly flexibilitu potřebnou pro vyvíjející se paketové služby. Díky poskytnutí struktury hlavičky nezávislé na přenosu usnadnila zavedení pokročilých služeb, jako je SMS přes GPRS, a připravila cestu pro zvýšené datové rychlosti s EDGE. Její návrh zajistil, že síťové prvky mohou správně zpracovávat bloky bez ohledu na rádiovou technologii nebo vývoj jádra sítě, čímž podpořila dlouhodobou škálovatelnost a spolehlivost mobilních datových sítí 2G/3G.

## Klíčové vlastnosti

- Standardizovaná struktura pro BSSGP protokolové datové jednotky
- Obsahuje Block Type pro rozlišení dat a signalizace
- Zahrnuje Block Length pro určení velikosti PDU
- Podporuje směrování prostřednictvím identifikátorů Network Service Entity (NSE) a Base Station System Virtual Connection (BVC)
- Umožňuje mechanismy řízení toku a zpracování chyb
- Usnadňuje multiplexování logických připojení přes rozhraní Gb

## Související pojmy

- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [BH na 3GPP Explorer](https://3gpp-explorer.com/glossary/bh/)
