---
slug: "pef"
url: "/mobilnisite/slovnik/pef/"
type: "slovnik"
title: "PEF – Policy Enforcement Function"
date: 2025-01-01
abbr: "PEF"
fullName: "Policy Enforcement Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pef/"
summary: "PEF (funkce vynucování pravidel) je síťová funkce, která vynucuje rozhodnutí o pravidlech pro uživatelské relace, jako je QoS, účtování a řízení přístupu. Zajišťuje, aby byly síťové zdroje přidělovány"
---

PEF (funkce vynucování pravidel) je síťová funkce, která vynucuje rozhodnutí o pravidlech pro uživatelské relace, jako je QoS, účtování a řízení přístupu, aby zajistila přidělování síťových zdrojů v souladu s politikami operátora.

## Popis

Policy Enforcement Function (PEF, funkce vynucování pravidel) je základní síťová komponenta definovaná ve specifikacích 3GPP, zejména v TS 23.228, jako součást architektury IP Multimedia Subsystem (IMS) a řízení pravidel. Funguje v rámci frameworku Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), kde spolupracuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) při uplatňování rozhodnutí o pravidlech na datové relace uživatelů. Architektura typicky umisťuje PEF na úroveň brány, například v Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G nebo v Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G, kde může zachytávat a manipulovat s datovými toky na základě pravidel přijatých od PCRF.

Při provozu přijímá PEF pravidla od PCRF přes rozhraní Gx (v 4G) nebo N7 (v 5G). Tato pravidla zahrnují instrukce pro parametry Quality of Service (QoS) (např. omezení šířky pásma, úrovně priority), účtovací akce (např. spouštěče online nebo offline účtování) a řízení přístupu (např. blokování nebo povolování konkrétních služeb). PEF pak tato pravidla vynucuje konfigurací funkcí uživatelské roviny, jako je detekce provozu, gating (povolování nebo zamítání paketů) a označování QoS. Například může aplikovat garantovaný přenosový výkon pro video stream nebo omezit šířku pásma pro aplikaci s nízkou prioritou. Klíčové komponenty PEF zahrnují Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)) pro identifikaci aplikačních toků a Enforcement Point ([EP](/mobilnisite/slovnik/ep/)), kde jsou pravidla fyzicky aplikována na pakety.

Role PEF v síti je klíčová pro dynamické řízení pravidel, což operátorům umožňuje nabízet diferencované služby a optimalizovat výkon sítě. Zajišťuje, že rozhodnutí o pravidlech jsou převedena na proveditelné změny v datové cestě, čímž podporuje případy užití jako sponzorovaná data, rodičovské kontroly a síťové segmenty (network slicing). Vynucováním pravidel v reálném čase pomáhá PEF udržovat smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), řídit přetížení a implementovat účtovací schémata. Ve vyvinutých architekturách, jako je Service-Based Architecture ([SBA](/mobilnisite/slovnik/sba/)) v 5G, je funkčnost PEF integrována do síťových funkcí, jako je SMF a User Plane Function (UPF), což poskytuje flexibilnější a škálovatelnější vynucování pravidel napříč různými službami.

## K čemu slouží

PEF byla vytvořena, aby řešila potřebu dynamické a detailní kontroly pravidel v mobilních sítích, protože služby se vyvinuly za hranice základního hlasu a SMS a zahrnují multimédia, přístup k internetu a IoT aplikace. Před její standardizací bylo vynucování pravidel často statické, pevně zakódované v síťovém zařízení, což omezovalo schopnost operátorů přizpůsobit se měnícím se vzorcům provozu nebo nabízet personalizované služby. Mezi omezení patřila nepružná správa QoS, nedostatek integrace účtování v reálném čase a obtíže při vynucování pravidel specifických pro služby, což vedlo k neefektivnímu využití zdrojů a sníženým příjmovým příležitostem.

Motivována růstem IMS a datových služeb ve 3GPP Release 2 a novějších, objevila se PEF jako součást frameworku PCC, aby umožnila operátorům řídit chování sítě na základě pravidel. Řeší problémy, jako je dynamické přidělování šířky pásma pro různé aplikace, implementace pravidel spravedlivého používání a integrace účtování s poskytováním služeb. Historicky měly rané mobilní sítě základní mechanismy pravidel, ale PEF poskytla standardizovaný, interoperabilní přístup, který oddělil rozhodování o pravidlech (v PCRF) od jejich vynucování (v PEF), což umožnilo flexibilnější a škálovatelnější správu sítě.

PEF také řeší provozní výzvy, jako je přetížení sítě a diferenciace služeb. Například s nástupem over-the-top (OTT) aplikací potřebovali operátor nástroje pro správu provozu bez zhoršení uživatelského zážitku. PEF to umožňuje vynucováním pravidel, která upřednostňují kritické služby nebo omezují ty nepodstatné. Její vývoj přes verze jako Rel-5 a Rel-6 přidal vylepšení pro hlubší kontrolu paketů a integraci s účtovacími systémy, což odráží trvající potřebu vyvážit síťovou efektivitu s inovacemi služeb. Poskytnutím centralizovaného bodu vynucování pomáhá PEF operátorům zpeněžit služby, zajistit kvalitu a udržet kontrolu nad svými sítěmi.

## Klíčové vlastnosti

- Vynucování pravidel QoS (např. šířka pásma, priorita)
- Integrace s účtovacími systémy pro online/offline účtování
- Detekce provozu a gating pro aplikační toky
- Podpora dynamických aktualizací pravidel od PCRF
- Řízení přístupu a autorizace služeb
- Interoperabilita s bránami jádra sítě (např. PGW, UPF)

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description

---

📖 **Anglický originál a plná specifikace:** [PEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pef/)
