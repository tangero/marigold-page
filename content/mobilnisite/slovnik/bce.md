---
slug: "bce"
url: "/mobilnisite/slovnik/bce/"
type: "slovnik"
title: "BCE – Billing and Charging Evolution"
date: 2025-01-01
abbr: "BCE"
fullName: "Billing and Charging Evolution"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bce/"
summary: "BCE je rámec 3GPP pro vývoj fakturačních a účtovacích systémů za účelem podpory nových služeb a obchodních modelů. Poskytuje standardizovaná rozhraní a architektury pro offline a online účtování, což"
---

BCE je rámec 3GPP pro vývoj fakturačních a účtovacích systémů se standardizovanými rozhraními, který umožňuje podporu nových služeb a flexibilní správu výnosů pro operátory.

## Popis

Billing and Charging Evolution (BCE) je komplexní rámec v rámci standardů 3GPP, který definuje architekturu, rozhraní a procedury pro modernizaci telekomunikačních fakturačních a účtovacích systémů. Je navržen tak, aby zvládal složitosti účtování širokého spektra služeb, včetně tradičního hlasu a [SMS](/mobilnisite/slovnik/sms/), datových služeb, služeb založených na IMS (jako VoLTE a VoNR) a nově vznikajících nabídek, jako je síťové dělení (network slicing) a IoT konektivita. Rámec podporuje jak offline účtování (pro předplatitele s platbou dodatečně), tak online účtování (pro předplacené služby nebo správu kreditu v reálném čase), což operátorům zajišťuje možnost implementovat flexibilní obchodní modely. Specifikace BCE, podrobně popsané především v dokumentech 3GPP TS 28.827 a TS 29.275, poskytují technické plány pro integraci účtovacích systémů s síťovými prvky, jako je Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)).

Architektonicky BCE navazuje na rámec Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) zavedený ve verzi 3GPP Release 7 a rozšiřuje jej o vylepšené možnosti pro účtování založené na službách. Mezi klíčové komponenty patří Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)), která sídlí v síťových prvcích (např. [P-GW](/mobilnisite/slovnik/p-gw/), [S-CSCF](/mobilnisite/slovnik/s-cscf/)), detekuje účtovatelné události a generuje Charging Data Records (CDR) pro offline účtování nebo žádá o autorizaci kreditu pro online účtování. Pro online účtování Online Charging System (OCS) komunikuje s CTF prostřednictvím referenčního bodu Ro (založeného na protokolu Diameter), aby prováděl správu kreditu v reálném čase, a povoluje nebo odmítá službu na základě stavu účtu předplatitele. Pro offline účtování CTF odesílá CDR záznamy prostřednictvím referenčního bodu Rf do funkce Charging Data Function (CDF), která je následně předává do funkce Charging Gateway Function (CGF) pro mediaci a následné zpracování pro fakturaci.

BCE funguje tak, že standardizuje tok účtovacích informací po síti. Když předplatitel zahájí službu, CTF identifikuje událost a uplatní účtovací pravidla přijatá od PCRF. Při online účtování CTF odešle žádost o řízení kreditu do OCS, který zkontroluje účet předplatitele, rezervuje kredit a odpoví autorizací. CTF pak sleduje využití prostředků a periodicky hlásí, dokud sezení neskončí nebo nedojde kredit, což spustí novou autorizaci nebo ukončení. Pro offline účtování CTF shromažďuje data o využití, formátuje je do CDR záznamů s podrobnostmi, jako je délka relace a objem dat, a přenáší je do CDF. Tyto záznamy jsou následně agregovány, korelovány a formátovány pro fakturační systémy. BCE také podporuje účtování založené na událostech pro jednorázové transakce (např. SMS) a účtování založené na relacích pro kontinuální služby (např. datové relace).

Role BCE v síti je klíčová pro monetizaci a provozní efektivitu. Umožňuje operátorům implementovat složité účtovací scénáře, jako je vrstvené ceny, sponzorovaná data a účtování založené na kvalitě služeb (QoS), tím, že poskytuje standardizovaný, interoperabilní rámec. To snižuje náklady na integraci a urychluje nasazení služeb. Vývoj BCE začlenil podporu pro virtualizaci síťových funkcí (NFV) a cloud-nativní architektury, což umožňuje účtovacím systémům dynamicky škálovat s poptávkou po síti. Oddělením účtovací logiky od síťových funkcí BCE usnadňuje inovace v nabídkách služeb a pomáhá operátorům konkurovat v rychle se měnícím telekomunikačním prostředí. Jeho specifikace zajišťují zpětnou kompatibilitu a zároveň umožňují pokročilé funkce, což z něj činí základní kámen ekosystému správy a účtování 3GPP.

## K čemu slouží

BCE bylo vytvořeno, aby řešilo omezení starších fakturačních a účtovacích systémů, které byly často proprietární, nepružné a nedokázaly držet krok s rychlým zaváděním nových služeb v sítích 3GPP. Před BCE byly účtovací mechanismy roztříštěné napříč různými síťovými doménami (např. přepojování okruhů vs. přepojování paketů), což vedlo ke složitým integracím a vysokým provozním nákladům. Růst datových služeb, IMS a později 5G si vyžádal jednotný, standardizovaný přístup, který by dokázal podporovat účtování v reálném čase, rozmanité obchodní modely a bezproblémovou interoperabilitu mezi síťovými prvky od více dodavatelů.

Historicky, jak se 3GPP vyvíjelo od Release 7 se zavedením PCC, bylo jasné, že účtovací systémy se musí vyvinout za pouhé generování CDR. Operátoři čelili výzvám při monetizaci inovativních služeb, jako je streamování videa, IoT aplikace a síťové řezy (network slices), které vyžadovaly dynamické, politikami řízené účtování. BCE bylo motivováno potřebou poskytnout rámec připravený na budoucnost, který by dokázal zvládnout tyto složitosti, a umožnit operátorům nabízet personalizované ceny, spravovat kredit v reálném čase a zkracovat dobu uvedení nových služeb na trh. Standardizací rozhraní jako Ro a Rf BCE vyřešilo problémy s interoperabilitou, což operátorům umožnilo efektivně kombinovat síťové a účtovací komponenty.

Dále BCE řeší posun směrem ke konvergovanému účtování, kde jsou online a offline účtování integrovány do jediného systému, jak je vidět v pozdějších verzích 3GPP. Tento vývoj podporuje trend obchodní inteligence v reálném čase a zapojení zákazníků, což operátorům umožňuje okamžitě reagovat na vzorce využívání a nabízet akční nabídky. Účel BCE sahá až k umožnění dodržování regulatorních požadavků, správě podvodů a podrobnému reportingu, což jej činí nezbytným pro moderní telekomunikační provozy. Bez BCE by operátoři zápasili s přizpůsobováním se požadavkům 5G a dalších generací, kde jsou služby dynamičtější a náročnější na prostředky.

## Klíčové vlastnosti

- Standardizovaná rozhraní (např. Ro, Rf) pro účtovací komunikaci
- Podpora jak offline účtování (založeného na CDR), tak online účtování (řízení kreditu v reálném čase)
- Integrace s rámcem Policy and Charging Control (PCC) pro dynamické uplatňování pravidel
- Flexibilní účtovací modely: založené na relaci, na události a na objemu/délce trvání
- Škálovatelnost prostřednictvím podpory virtualizovaných a cloud-nativních architektur
- Zpětná kompatibilita a vývoj směrem ke konvergovaným účtovacím systémům

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TR 28.827** (Rel-18) — Technical Report on 5G Charging for Roaming Scenarios
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [BCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bce/)
