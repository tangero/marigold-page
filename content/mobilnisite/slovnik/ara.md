---
slug: "ara"
url: "/mobilnisite/slovnik/ara/"
type: "slovnik"
title: "ARA – Aggregated RUCI Report Answer"
date: 2025-01-01
abbr: "ARA"
fullName: "Aggregated RUCI Report Answer"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ara/"
summary: "ARA je zpráva řídicího protokolu definovaná v 3GPP pro řízení politiky a účtování (PCC). Jedná se o odpověď od funkce pro pravidla politiky a účtování (PCRF) směrem k funkci pro detekci provozu (TDF),"
---

ARA je zpráva protokolu PCC z PCRF do TDF, která potvrzuje agregované hlášení událostí v uživatelské rovině pro účely politiky a účtování.

## Popis

Aggregated RUCI Report Answer (ARA) je zpráva protokolu založeného na Diameteru specifikovaná v architektuře 3GPP pro řízení politiky a účtování (PCC), primárně dokumentovaná v TS 29.213 a TS 29.217. Funguje na referenčním bodu Sd, což je rozhraní mezi funkcí pro detekci provozu (TDF) a funkcí pro pravidla politiky a účtování (PCRF). ARA je klíčovou součástí funkce Application Detection and Control ([ADC](/mobilnisite/slovnik/adc/)), která síti umožňuje monitorovat a vynucovat politiky na provoz konkrétních aplikací v uživatelské rovině.

Architektonicky je TDF zodpovědné za kontrolu datového provozu uživatele, identifikaci konkrétních aplikací nebo služeb (např. streamování videa, sociální sítě) a hlášení těchto událostí PCRF. PCRF je centrální entita pro rozhodování o politikách, která určuje, jak má být s provozem nakládáno z hlediska QoS, povolování a účtování. Když TDF odešle PCRF požadavek Aggregated RUCI Report Request ([ARR](/mobilnisite/slovnik/arr/)), poskytne konsolidovanou zprávu o více událostech v uživatelské rovině, jako jsou spuštění nebo zastavení aplikace nebo dosažení prahových objemů dat, pro jednu nebo více uživatelských relací. ARA je odpověď PCRF na tento požadavek, která potvrzuje příjem a poskytuje TDF případné potřebné instrukce nebo potvrzení.

Zpráva ARA obsahuje několik klíčových [AVP](/mobilnisite/slovnik/avp/) (párů atribut-hodnota), které zajišťují její funkci. Patří mezi ně Session-Id, který identifikuje konkrétní relaci Diameter; Origin-Host a Origin-Realm identifikující PCRF; a Result-Code udávající úspěch nebo selhání zpracování ARR. Může také obsahovat AVP Charging-Rule-Report, pokud PCRF potřebuje na základě agregované zprávy aktualizovat nebo odebrat účtovací pravidla, nebo AVP Event-Trigger, aby TDF instruovala ohledně nových spouštěčů hlášení. Zpráva zajišťuje, že PCRF a TDF mají synchronizovaný pohled na aktivitu uživatele, což umožňuje dynamické úpravy politik.

Během provozu ARA dokončuje transakci zahájenou periodickým nebo událostmi spouštěným hlášením z TDF. Agregací více událostí do jedné zprávy (ARR) systém snižuje signalizační režii ve srovnání s hlášením každé události jednotlivě. PCRF tato agregovaná data zpracuje, zkoreluje je s politikami předplatitele a odpoví pomocí ARA. Tato odpověď může obsahovat nová rozhodnutí o politikách, jako je změna šířky pásma, aplikování tvarování provozu nebo spuštění účtovacích událostí. ARA tedy hraje zásadní roli při umožnění efektivního vynucování politik v reálném čase na základě povědomí o aplikacích, což přispívá k optimalizovanému využití síťových prostředků a lepší uživatelské zkušenosti.

## K čemu slouží

ARA byla zavedena, aby řešila rostoucí potřebu inteligentního řízení politik založeného na povědomí o aplikacích v mobilních sítích, zejména s nástupem různorodých Over-The-Top ([OTT](/mobilnisite/slovnik/ott/)) aplikací. Před jejím zavedením bylo řízení politik v sítích 3GPP založeno primárně na atributech na úrovni přenosového kanálu (např. [APN](/mobilnisite/slovnik/apn/), QoS) spíše než na hluboké kontrole paketů (DPI) obsahu aplikací. Toto omezení ztěžovalo operátorům implementaci podrobných politik pro konkrétní služby, jako je blokování nebo omezování určitých aplikací, nabídka sponzorovaných dat nebo aplikace diferencovaného účtování.

Vytvoření funkce Application Detection and Control ([ADC](/mobilnisite/slovnik/adc/)) ve verzi 13, která zahrnuje ARA, bylo motivováno požadavky operátorů na sofistikovanější možnosti správy provozu. TDF fungující jako DPI engine mohlo aplikace detekovat, ale efektivní komunikace s PCRF byla nezbytná. ARA jako součást protokolu rozhraní Sd řeší problém efektivity signalizace tím, že umožňuje agregované hlášení. Namísto odesílání samostatné zprávy pro každou jednotlivou událost aplikace (což by vytvořilo nadměrnou signalizační zátěž) TDF sdruží více událostí do Aggregated RUCI Report Request. ARA poskytuje potřebné potvrzení a případné aktualizace politik od PCRF, což zajišťuje efektivní škálovatelnost systému i při vysokých objemech aplikačního provozu.

Tento mechanismus umožňuje operátorům zavádět pokročilé nabídky služeb, jako je zero-rating pro konkrétní aplikace, rodičovské kontroly nebo podnikové tarify, bez zahlcení jádra sítě signalizací. Také podporuje soulad s regulatorními požadavky na správu provozu. Tím, že poskytuje standardizovaný způsob zpracování agregovaných hlášení o aplikacích, ARA usnadňuje interoperabilitu mezi zařízeními různých výrobců pro TDF a PCRF, podporuje více-dodavatelský ekosystém a umožňuje konzistentní vynucování politik v celé síti.

## Klíčové vlastnosti

- Zpráva protokolu založeného na Diameteru na rozhraní Sd
- Odpověď na Aggregated RUCI Report Request (ARR) z TDF
- Umožňuje potvrzení agregovaných hlášení o událostech aplikací
- Podporuje dynamické aktualizace politik od PCRF směrem k TDF
- Snižuje signalizační režii prostřednictvím agregace událostí
- Integrální součást funkce 3GPP Application Detection and Control (ADC)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface

---

📖 **Anglický originál a plná specifikace:** [ARA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ara/)
