---
slug: "ram"
url: "/mobilnisite/slovnik/ram/"
type: "slovnik"
title: "RAM – Remote Application Management"
date: 2026-01-01
abbr: "RAM"
fullName: "Remote Application Management"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ram/"
summary: "Remote Application Management (RAM) je 3GPP rámec pro vzdálenou provizi, konfiguraci a správu životního cyklu aplikací na uživatelském zařízení (UE). Umožňuje síťovým operátorům a poskytovatelům služe"
---

RAM je 3GPP rámec pro vzdálenou provizi, konfiguraci a správu životního cyklu aplikací na uživatelském zařízení.

## Popis

Remote Application Management (RAM) je standardizovaný rámec definovaný 3GPP pro vzdálenou správu aplikací umístěných na uživatelském zařízení (UE). Funguje jako klíčová součást širšího ekosystému správy zařízení, často spolupracuje s protokoly jako [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/) (Open Mobile Alliance Device Management) nebo využívá vlastní architekturu správy 3GPP. Hlavní funkcí RAM je umožnit Management Serveru, typicky provozovanému síťovým operátorem nebo autorizovaným poskytovatelem služeb, provádět operace životního cyklu na aplikacích nainstalovaných na UE. To zahrnuje provizi nových aplikací, aktualizaci či opravu stávajících, konfiguraci aplikačních parametrů a deaktivaci nebo odstranění aplikací, vše prováděné přes mobilní síť bez nutnosti fyzického přístupu k zařízení.

Architektura zahrnuje několik logických entit: RAM Server (neboli Management Server), RAM Klient na UE a samotné spravované aplikace. RAM Klient funguje jako agent na zařízení, který přijímá příkazy správy ze serveru přes zabezpečenou správní relaci. Tyto příkazy jsou definovány pomocí specifického správního protokolu a datového modelu, které popisují akce, které mají být provedeny na aplikačních objektech. Správní objekty pro aplikace mohou obsahovat informace jako identifikátor aplikace, verze, zdroj instalace ([URI](/mobilnisite/slovnik/uri/)), stav aktivace a konfigurační parametry. Rámec RAM zajišťuje, že tyto operace jsou prováděny kontrolovaným způsobem s ohledem na zabezpečení, souhlas uživatele (je-li relevantní) a omezení zdrojů zařízení.

RAM hraje klíčovou roli v moderních telekomunikačních sítích tím, že umožňuje dynamické nasazování služeb. Pro služby jako IP Multimedia Subsystem (IMS), Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) nebo různé vertikální IoT aplikace je schopnost vzdáleně provizionovat a konfigurovat potřebný klientský software zásadní pro škálovatelná nasazení a průběžný vývoj služeb. Odděluje životní cyklus aplikace od aktualizací firmware nebo operačního systému zařízení, což umožňuje častější a cílenější vylepšení služeb. Specifikace pokrývající RAM, jako je TS 26.237 pro služby IMS nebo TS 33.117 pro zabezpečení, definují podrobné procedury, datové modely a bezpečnostní mechanismy pro zajištění interoperabilní a bezpečné vzdálené správy napříč různými výrobci a typy zařízení.

## K čemu slouží

Účelem Remote Application Management (RAM) je řešit provozní výzvu manuální správy softwarových aplikací na masivním množství nasazených zařízení. Před takovou standardizací často aktualizace nebo konfigurace aplikace na mobilním zařízení vyžadovala uživatelem iniciované stahování z obchodu s aplikacemi nebo těžkopádné procesy ruční instalace, což bylo pro služby spravované operátorem neefektivní. Pro síťové operátory a podniky nabízející specializované služby (např. komunikace pro kritické mise, IoT řešení) byl tento manuální model neudržitelný, což vedlo k fragmentovaným verzím softwaru, bezpečnostním zranitelnostem a vysokým nákladům na podporu.

RAM byl zaveden, aby poskytl standardizovaný, síťově orientovaný mechanismus pro správu aplikací přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)). To umožňuje poskytovatelům služeb zajistit, že na zařízení uživatele je nainstalována správná verze služebně specifické aplikace a je řádně nakonfigurována, což garantuje kompatibilitu a výkon služby. Je to zvláště motivováno nástupem složitých, na síti závislých služeb, jako je Voice over LTE (VoLTE) a služby pro kritické mise, kde musí klientská aplikace úzce spolupracovat se síťovými funkcemi. RAM poskytuje nástroje pro spolehlivé nasazení a údržbu těchto klientů.

Tím, že umožňuje vzdálenou správu, RAM řeší omezení v agilitě a zabezpečení. Umožňuje rychlé nasazení oprav chyb a bezpečnostních záplat, což je klíčové pro zmírnění zranitelností. Také podporuje provizi konfiguračních dat specifických pro síťového operátora, čímž zajišťuje optimální chování služby. Nakonec RAM snižuje celkové náklady na vlastnictví spravovaných služeb a zlepšuje uživatelský zážitek tím, že zajišťuje bezproblémový provoz služeb ihned po vybalení a jejich automatické udržování v aktuálním stavu.

## Klíčové vlastnosti

- Provize a instalace aplikací přes vzdušné rozhraní (OTA)
- Vzdálená správa aktualizací a záplat pro nainstalované aplikace
- Správa konfigurace aplikačních parametrů a nastavení
- Řízení životního cyklu aplikace (aktivace, deaktivace, odstranění)
- Podpora správy závislostí mezi aplikacemi
- Zabezpečené správní protokoly a autorizační mechanismy

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 26.073** (Rel-19) — AMR Speech Codec ANSI-C Implementation
- **TS 26.104** (Rel-19) — AMR Floating-Point Codec Implementation
- **TS 26.173** (Rel-19) — AMR-WB Codec ANSI-C Implementation
- **TS 26.204** (Rel-19) — AMR-WB Floating-Point Codec Specification
- **TS 26.243** (Rel-19) — DSR Extended Advanced Front-end C Code
- **TS 26.268** (Rel-19) — eCall In-band Modem ANSI-C Code
- **TS 26.273** (Rel-19) — Fixed-point AMR-WB+ codec ANSI-C code
- **TS 26.304** (Rel-19) — Floating-point Extended AMR-WB+ Codec ANSI-C Code
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [RAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ram/)
