---
slug: "i-bgf"
url: "/mobilnisite/slovnik/i-bgf/"
type: "slovnik"
title: "I-BGF – Interconnection-Border Gateway Function"
date: 2025-01-01
abbr: "I-BGF"
fullName: "Interconnection-Border Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/i-bgf/"
summary: "Funkční entita v subsystému IP multimédií (IMS), která slouží jako hraniční brána pro propojení mezi různými sítěmi operátorů nebo mezi sítí IMS a jinými IP sítěmi. Řídí toky médií, poskytuje překlad"
---

I-BGF je hraniční brána IMS, která řídí média, poskytuje NAPT a vynucuje bezpečnostní a QoS politiky pro propojení mezi sítěmi operátorů nebo jinými IP sítěmi.

## Popis

Funkce hraniční brány pro propojení (I-BGF) je klíčová síťová funkce definovaná v architektuře subsystému IP multimédií (IMS) podle 3GPP, specifikovaná v dokumentech jako TS 23.228 a TS 29.421. Nachází se na hranici mezi IMS sítí operátora a externími IP sítěmi, což může být jiná IMS síť od jiného operátora, sít s přepojováním okruhů přes mediální bránu nebo veřejný internet. Jejím hlavním úkolem je sloužit jako řízená brána pro multimediální IP provoz (hlas, video) a vynucovat politiky operátora pro mediální relace překračující administrativní hranice.

Architektonicky je I-BGF funkcí v rovině médií, kterou řídí funkce signalizační roviny, typicky funkce řídicí brány pro průnik ([BGCF](/mobilnisite/slovnik/bgcf/)) nebo řídicí funkce hraničního kontroléru relací (SBC). Pro toto řízení implementuje rozhraní Go (založené na protokolu H.248), přes které přijímá pokyny, které mediální toky povolit, upravit nebo blokovat. I-BGF provádí hlubokou kontrolu a manipulaci paketů v tocích protokolu pro přenos v reálném čase (RTP) a jeho řídicího protokolu (RTCP), které přenášejí vlastní hlasová a video data.

Mezi klíčové operace I-BGF patří překlad síťových adres a portů ([NAPT](/mobilnisite/slovnik/napt/)), který skrývá vnitřní topologii a adresaci domovské sítě před externími účastníky. Dynamicky otevírá a zavírá otvory (pinholes) ve firewallu na základě signalizace relace, čímž povoluje mediální toky pouze pro autorizované relace. Dále provádí vynucování šířky pásma a označování paketů pro zajištění dodržování kvality služeb (QoS) a v případě potřeby může provádět transkódování mediálních kodeků, aby zajistila interoperabilitu mezi sítěmi s různými podporovanými sadami kodeků. Navíc poskytuje podrobné účetní informace pro účely fakturace, zaznamenává například objem přenesených dat na relaci.

I-BGF je v podstatě místem vynucení mediální politiky IMS sítě na jejím okraji. Zajišťuje, aby přes hranici procházel pouze legitimní, signalizovaný mediální provoz, chrání vnitřní síťové zdroje, poskytuje funkce interoperability a umožňuje přesné účtování služeb propojení. Je základní součástí pro bezpečné a komerční propojení služeb založených na IP.

## K čemu slouží

I-BGF byla zavedena, aby řešila výzvy spojené s propojováním IP multimediálních sítí, zejména když operátoři začali nasazovat IMS pro služby jako Voice over LTE (VoLTE) a Rich Communication Services (RCS). Před standardizovanými hraničními funkcemi bylo propojení mezi IP sítěmi často řešeno jednoduchými směrovači nebo nestandardizovanými hraničními kontroléry relací (SBC), což vedlo k problémům s interoperabilitou, bezpečnostním rizikům a obtížím při zavádění jednotných politik a účtování.

Její vytvoření bylo motivováno potřebou standardizované, politikami řízené hraniční funkce v rámci architektury IMS. Řeší problém zabezpečení okraje sítě tím, že funguje jako firewall a zařízení s [NAPT](/mobilnisite/slovnik/napt/) speciálně navržené pro dynamické multimediální relace. Bez I-BGF by byla IMS síť vystavena neautorizovanému mediálnímu provozu, útokům typu denial-of-service a potenciálnímu odhalení topologie externími subjekty.

Dále I-BGF umožňuje komerční propojení mezi operátory tím, že poskytuje nezbytné funkce pro vynucování QoS a podrobné účtování. Umožňuje operátorům vyjednávat smlouvy o úrovni služeb (SLA) a mít technický prostředek k jejich vynucení na úrovni médií. Také usnadňuje interoperabilitu tím, že zvládá potřebné signalizační a mediální adaptace mezi různými implementacemi sítí nebo jejich generacemi, což z IMS činí životaschopnou technologii pro globální nasazení služeb.

## Klíčové vlastnosti

- Řídí tok médií (RTP/RTCP) na hranici propojení na základě signalizace relace.
- Provádí překlad síťových adres a portů (NAPT) pro skrytí vnitřní topologie sítě.
- Poskytuje funkci firewallu dynamickým otevíráním/zavíráním otvorů (pinholes) pro autorizované relace.
- Vynucuje politiky kvality služeb (QoS) prostřednictvím vynucování šířky pásma a označování paketů.
- Podporuje transkódování mediálních kodeků pro interoperabilitu mezi různými sítěmi.
- Generuje podrobné účetní údaje (např. přenesené bajty) pro účtování propojení.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [BGCF – Breakout Gateway Control Function](/mobilnisite/slovnik/bgcf/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks

---

📖 **Anglický originál a plná specifikace:** [I-BGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-bgf/)
