---
slug: "nsce"
url: "/mobilnisite/slovnik/nsce/"
type: "slovnik"
title: "NSCE – Network Slice Capability Enablement"
date: 2026-01-01
abbr: "NSCE"
fullName: "Network Slice Capability Enablement"
category: "Network Slicing"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nsce/"
summary: "Rámec pro zpřístupnění a vystavení schopností síťových řezů aplikacím a vertikálám. Umožňuje aplikacím objevovat, požadovat a využívat specifické funkce řezů, čímž překlenuje propast mezi síťovou funk"
---

NSCE je rámec pro zpřístupnění a vystavení schopností síťových řezů aplikacím, umožňující jim objevovat, požadovat a využívat specifické funkce řezů.

## Popis

Network Slice Capability Enablement (NSCE) je komplexní rámec zavedený ve specifikaci 3GPP Release 17, který usnadňuje interakci mezi aplikacemi (nebo systémy vertikálních odvětví) a základními schopnostmi 5G síťových řezů. Funguje jako mezivrstva, která překládá aplikační požadavky vysoké úrovně na specifické parametry pro výběr a konfiguraci síťového řezu, kterým 5G core síť rozumí a může je poskytnout. Architektura zahrnuje několik klíčových funkčních komponent, především NSCE Capability Exposure Function (NSCE-CEF) a NSCE Application Function (NSCE-AF). NSCE-CEF je zodpovědná za vystavení schopností sítě, jako jsou dostupné typy řezů, výkonnostní charakteristiky (latence, šířka pásma) a pokrytí servisní oblasti, autorizovaným externím subjektům. NSCE-AF, nacházející se v aplikační doméně, formuluje požadavky na služby na základě potřeb aplikace a komunikuje s NSCE-CEF prostřednictvím standardizovaných [API](/mobilnisite/slovnik/api/), jako jsou například ta definovaná v TS 29.549.

Pracovní postup začíná objevováním schopností, kdy aplikace dotazuje NSCE-CEF, aby zjistila, jaké schopnosti řezů jsou dostupné v dané geografické oblasti. Na základě této informace může aplikace následně požádat o zpřístupnění konkrétní instance síťového řezu nebo o využití existujícího řezu, který odpovídá jejím požadavkům. Rámec NSCE zajišťuje mapování parametrů na aplikační úrovni (např. 'ultraspolehlivá komunikace s nízkou latencí pro tovární automatizaci') na technické informace pro asistenci při výběru síťového řezu ([NSSAI](/mobilnisite/slovnik/nssai/)) a potenciálně interaguje s Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) v rámci 5G core, aby zajistil výběr vhodného řezu a uplatnění příslušných politik pro uživatelské zařízení (UE). Tento proces zahrnuje aspekty správy životního cyklu, umožňující modifikaci nebo ukončení využití řezu, jak se vyvíjejí aplikační relace.

Role NSCE je klíčová pro plné využití ekonomického potenciálu 5G síťových řezů pro vertikální odvětví. Překračuje rámec prostého poskytování řezů operátorem a umožňuje dynamický, poptávkou řízený model, kde se aplikace mohou aktivně účastnit procesu výběru a konfigurace řezu. To vyžaduje robustní mechanismy autentizace, autorizace a účtování ([AAA](/mobilnisite/slovnik/aaa/)), jak jsou definovány v příslušných bezpečnostních specifikacích, aby bylo zajištěno, že k síťovým prostředkům mohou přistupovat a je ovládat pouze autorizované aplikace. Poskytnutím standardizovaného rozhraní pro vystavení schopností řezů NSCE snižuje složitost integrace pro vývojáře aplikací a umožňuje nové obchodní modely, jako je slice-as-a-service, kde mohou vertikály na požádání získat přístup k přizpůsobeným zárukám síťového výkonu.

## K čemu slouží

NSCE bylo vytvořeno, aby vyřešilo kritický nedostatek v původní architektuře 5G síťových řezů definované v Release 15 a 16. Zatímco tato vydání standardizovala základní mechanismy pro vytváření a správu síťových řezů v rámci domény operátora, poskytovala pouze omezené, nestandardizované prostředky pro interakci externích aplikací a zákazníků z vertikálních odvětví s těmito řezy. Absence standardizovaného expozičního rozhraní znamenala, že každý operátor musel vyvíjet vlastní [API](/mobilnisite/slovnik/api/), což vedlo k fragmentaci, vysokým integračním nákladům pro poskytovatele aplikací a neschopnosti vytvářet přenositelné aplikace napříč různými operátorskými sítěmi. To bránilo komercializaci síťových řezů, zejména pro podnikové a IoT případy užití, které vyžadují programový přístup k síťovým prostředkům.

Primární problém, který NSCE řeší, je nespojitost mezi technickou implementací síťových řezů a obchodní nebo servisní logikou aplikací. Před NSCE musel podnik často absolvovat zdlouhavé manuální procesy s operátorem, aby získal řez se specifickými charakteristikami. NSCE tuto interakci automatizuje a standardizuje, což umožňuje aplikacím dynamicky objevovat a požadovat síťové schopnosti odpovídající jejich potřebám v reálném čase. To je nezbytné pro případy užití, jako jsou automaticky řízená vozidla ([AGV](/mobilnisite/slovnik/agv/)) v chytré továrně, kde aplikační software potřebuje garantovat určitou úroveň síťového výkonu před zahájením kritické operace. Motivací bylo odemknout výnosový potenciál 5G pro operátory tím, že se řezy stanou snadno využitelnými, což podpoří ekosystém aplikací s povědomím o řezech a urychlí adopci 5G ve vertikálních trzích, jako je výroba, zdravotnictví a doprava.

## Klíčové vlastnosti

- Standardizovaná API pro vystavení schopností (např. Nnscf_NSCE_CapabilityExposure) pro objevování dostupných typů síťových řezů a jejich atributů.
- Rozhraní pro dynamický požadavek na zpřístupnění řezu umožňující aplikacím požadovat aktivaci nebo využití konkrétní instance síťového řezu.
- Mapování aplikačních požadavků na služby na parametry pro výběr síťového řezu definované 3GPP (S-NSSAI, DNN).
- Integrace s funkcemi core sítě (NSSF, PCF) pro výběr řezu a uplatnění politik na základě požadavků aplikace.
- Podpora vystavení schopností řezů podle geografické oblasti, umožňující poskytování služeb s ohledem na polohu.
- Správa životního cyklu asociace mezi aplikační relací a síťovým řezem, včetně modifikace a ukončení.

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 29.435** (Rel-19) — SEAL NSCE Server Services Stage 3
- **TS 29.536** (Rel-19) — NSACF Service Based Interface Protocol
- **TS 29.548** (Rel-19) — SEAL Data Delivery Server Services Stage 3
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications

---

📖 **Anglický originál a plná specifikace:** [NSCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsce/)
