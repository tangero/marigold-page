---
slug: "vs-rms"
url: "/mobilnisite/slovnik/vs-rms/"
type: "slovnik"
title: "VS-RMS – Vendor-Specific Remote Management Server"
date: 2025-01-01
abbr: "VS-RMS"
fullName: "Vendor-Specific Remote Management Server"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vs-rms/"
summary: "Serverová komponenta v systému správy 5G, která zpracuje vendor-specific rozšíření pro správu síťových funkcí. Umožňuje dodavatelům poskytovat proprietární schopnosti správy, jako například specializo"
---

VS-RMS je server v systému správy 5G, který zpracuje vendor-specific rozšíření a umožňuje proprietární schopnosti správy, jako například specializované sledování poruch nebo výkonu, aby doplnil standardizovaný framework.

## Popis

Vendor-Specific Remote Management Server (VS-RMS) je entita správy definovaná v architektuře správy 3GPP 5G, specifikovaná v TS 28.304, 28.305 a 32.972. Funguje jako část širšího ekosystému Management Function ([MF](/mobilnisite/slovnik/mf/)), který zahrnuje Network Resource Model ([NRM](/mobilnisite/slovnik/nrm/)) a související služby správy. VS-RMS je zodpovědný za hostování a zpřístupňování vendor-specific služeb správy a informačních modelů, které nejsou pokryty standardizovaným NRM. Funguje jako prostředník nebo specializovaný endpoint, který může systém správy, například Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management System ([EMS](/mobilnisite/slovnik/ems/)), dotazovat pro získání proprietárních dat nebo provedení vendor-specific operací správy na síťových funkcích (NFs).

Architektonicky VS-RMS komunikuje s standardizovaným frameworkem správy, typicky pomocí RESTful [API](/mobilnisite/slovnik/api/) na základě [HTTP](/mobilnisite/slovnik/http/)/2, podle principů service-based architektury 3GPP. Obsahuje vendor-specific Managed Object ([MO](/mobilnisite/slovnik/mo/)) třídy a jejich asociované atributy, operace a notifikace. Když systém správy potřebuje komunikovat s proprietárními funkcemi dodavatele – například pro sledování custom hardware senzorů, aplikaci vendor-specific optimalizační politiky nebo získání detailních diagnostických logů v proprietárním formátu – posílá management requesty na VS-RMS asociovaný s síťovou funkcí tohoto dodavatele. VS-RMS pak převádí tyto requesty na příkazy nebo dotazy pochopitelné implementací dodavatele a vrací odpovědi ve strukturovaném formátu.

Jak funguje zahrnuje jasné rozdělení odpovědností. Standardizovaný NRM poskytuje common interface pro všechny základní úlohy správy, zajišťuje multi-vendor interoperabilitu. VS-RMS rozšiřuje tento model pro vendor-unique schopnosti. V praxi systém správy zjistí existenci a schopnosti VS-RMS prostřednictvím standardizovaných management interfaces. Veškerá komunikace pro vendor-specific aspekty je pak směřována na tento server. Tento design udržuje core management data čisté a interoperabilní, zatímco poskytuje specializovaný, dobře definovaný kanál pro inovace. VS-RMS má klíčovou roli v umožnění pokročilých, vendor-differentiated schopností operational support systems ([OSS](/mobilnisite/slovnik/oss/)), jako například AI-driven prediktivní maintenance, custom performance analytics nebo specializované security hardening funkce, které jsou klíčové pro operátory, kteří hledají optimalizovaný síťový výkon mimo standardní specifikace.

## K čemu slouží

VS-RMS byl vytvořen pro řešení kritického problému správy síťů 5G: jak umožnit dodavatelům nabízet pokročilé, proprietární funkce správy bez fragmentace standardizované management plane. S příchodem 5G a cloud-native, software-based síťových funkcí a service-based architektury správy se potřeba flexibilní a extensible správy stala klíčovou. Pouze standardizovaný Network Resource Model (NRM) nemohl pokrýt každé vendor-unique hardware implementaci, software optimalizaci nebo inovativní feature set.

Historický kontext pochází z limitů předchozích systémů správy, kde vendor rozšíření byly často implementovány ad-hoc způsobem, vedoucí ke integrační komplexnosti a 'vendor lock-in' na management layer. VS-RMS, uvedený v Release 15 jako část holistického designu systému 5G, poskytuje formalizovanou, standards-based 'plugin' architekturu pro správu. Řeší problém definováním jasného boundary a interface pro vše vendor-specific. To umožňuje operátorům používat common NMS pro standardní úlohy v multi-vendor deployments, zatímco mohou využívat hluboké, vendor-specific schopnosti správy, které mohou poskytnout superior performance monitoring, fault resolution a lifecycle management pro equipment každého dodavatele.

Motivace byla podpora inovací v síťových operacích a automatizaci (Zero-touch network and Service Management - ZSM) při zachování manageability. Poskytnutím tohoto sanctioned outlet pro vendor rozšíření, 3GPP motivoval dodavatele k vývoji sophisticated OSS funkcí – jako například custom key performance indicator (KPI) kolekce, proprietární healing scripts nebo hardware-specific diagnostika – které poskytují competitive advantage. Pro operátory to znamená, že mohou využívat těchto pokročilých nástrojů bez ztráty schopnosti spravovat jejich síť prostřednictvím unified, standards-based interface, dosahující tak inovace i operational efficiency.

## Klíčové vlastnosti

- Hostuje vendor-specific informační modely a služby správy
- Integruje se s 3GPP 5G service-based architekturou správy
- Poskytuje RESTful API pro proprietární operace správy
- Umožňuje pokročilé, vendor-differentiated schopnosti OSS
- Udržuje separaci od standardizovaného NRM pro interoperabilitu
- Usnadňuje zjištění a přístup k vendor-unique managed objects

## Definující specifikace

- **TS 28.304** (Rel-19) — PEE Parameters Control & Monitoring Requirements
- **TS 28.305** (Rel-19) — PEE Control & Monitoring IRP Information Service
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks

---

📖 **Anglický originál a plná specifikace:** [VS-RMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vs-rms/)
