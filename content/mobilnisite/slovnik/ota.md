---
slug: "ota"
url: "/mobilnisite/slovnik/ota/"
type: "slovnik"
title: "OTA – Over The Air"
date: 2025-01-01
abbr: "OTA"
fullName: "Over The Air"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ota/"
summary: "Metoda bezdrátového distribuce softwaru, firmwaru, konfigurace nebo kryptografických aktualizací do zařízení. V rámci 3GPP zajišťuje, že zařízení lze dálkově spravovat, zabezpečovat a udržovat aktuáln"
---

OTA (Over The Air, česky přenos vzduchem) je metoda bezdrátového distribuce softwaru, firmwaru, konfigurace nebo kryptografických aktualizací do zařízení, která umožňuje jejich dálkovou správu, zabezpečení a kompatibilitu s požadavky sítě.

## Popis

Over The Air (OTA, česky přenos vzduchem) v kontextu 3GPP označuje mechanismy a postupy pro dálkovou, bezdrátovou správu uživatelského zařízení (UE). To zahrnuje širokou škálu funkcí, včetně aktualizací firmwaru (FOTA), aktualizací softwaru (SOTA), správy aplikací, konfigurace zařízení a poskytování autentizačních přihlašovacích údajů (např. pro eSIM). Proces je řízen síťovými OTA platformami, které komunikují s UE pomocí standardizovaných protokolů přes rozhraní buněčného rádiového přístupu.

Z architektonického hlediska OTA systém zahrnuje několik klíčových komponent. OTA server, provozovaný operátorem mobilní sítě ([MNO](/mobilnisite/slovnik/mno/)), výrobcem zařízení nebo poskytovatelem služeb, hostí balíčky aktualizací a spravuje kampaně jejich doručování. UE obsahuje OTA klientský agent zodpovědný za přijímání oznámení, stahování balíčků, ověřování jejich integrity a autenticity (často pomocí digitálních podpisů) a provádění aktualizačního procesu. Komunikace obvykle probíhá prostřednictvím IP protokolů (např. [HTTPS](/mobilnisite/slovnik/https/)) přenášených přes datové přenosy buněčné sítě. U kritických aktualizací, jako je firmware, je proces pečlivě rozdělen do fází: UE stáhne balíček, uloží jej do zabezpečené části, ověří jej a poté se restartuje do zabezpečeného režimu pro aplikaci aktualizace, čímž se zajišťuje odolnost proti výpadku napájení.

Jak to funguje, zahrnuje push nebo pull model. Server může zahájit relaci odesláním oznamovací zprávy do UE (např. přes [SMS](/mobilnisite/slovnik/sms/) nebo vyhrazený [NAS](/mobilnisite/slovnik/nas/) transport). UE poté naváže datové spojení na zadanou [URL](/mobilnisite/slovnik/url/) adresu pro stažení balíčku. Specifikace 3GPP definují bezpečnostní rámce pro ochranu OTA transakcí, které zajišťují, že balíčky nejsou pozměněny a že aktualizace mohou iniciovat pouze autorizované servery. V oblasti testování [RF](/mobilnisite/slovnik/rf/) výkonu se termín 'OTA' také vztahuje k radiačnímu testování Over-the-Air, při kterém se v anechoické komoře měří celkový vyzářený výkon ([TRP](/mobilnisite/slovnik/trp/)) a celková izotropní citlivost (TIS) zařízení. Uvedená definice '[REFSENS](/mobilnisite/slovnik/refsens/) RoAoA' je specifická metrika OTA testování pro určení kontury citlivosti přijímače vzhledem k referenčnímu směru, což je klíčové pro charakterizaci výkonu antény v zařízeních.

## K čemu slouží

Technologie OTA byla vytvořena, aby vyřešila masivní logistický a nákladový problém fyzické manipulace s miliony zařízení za účelem aktualizací. Před OTA vyžadovalo opravení softwarové chyby, aplikace bezpečnostní záplaty nebo povolení nové síťové funkce, aby uživatelé přinesli zařízení do servisních center nebo je ručně připojili k počítači, což vedlo k nízké penetraci aktualizací a prodlouženým bezpečnostním rizikům.

3GPP standardizovalo postupy OTA, aby umožnilo efektivní, škálovatelnou a bezpečnou dálkovou správu zařízení. Tím se řeší kritické provozní potřeby: udržování síťové kompatibility s vývojem standardů (např. od 4G k 5G), zavádění kritických bezpečnostních záplat pro ochranu sítě a uživatelských dat a umožnění nových servisních funkcí bez výměny hardwaru. Motivací bylo zlepšení uživatelského zážitku, snížení nákladů na podporu pro operátory a výrobce a zajištění dlouhodobé bezpečnosti a funkčnosti masivního ekosystému zařízení připojených k buněčné síti. OTA je zásadní pro správu životního cyklu všeho od chytrých telefonů po IoT senzory.

## Klíčové vlastnosti

- Zabezpečené stažení a ověření aktualizačních balíčků pomocí digitálních podpisů
- Podpora Firmware-Over-The-Air (FOTA) a Software-Over-The-Air (SOTA)
- Robustní aktualizační postupy s možností vrácení zpět v případě selhání
- Protokoly pro správu zařízení pro dálkovou konfiguraci a řízení
- Zřizování profilů eSIM (Remote SIM Provisioning)
- Standardizované metriky OTA testování pro RF výkon zařízení (např. TRP, TIS, REFSENS)

## Související pojmy

- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 23.875** (Rel-5) — Feasibility Study for Push Services Architecture
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 25.144** (Rel-11) — UE OTA Antenna Performance Requirements
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TS 29.544** (Rel-19) — Nspaf Service Based Interface (SP-AF) Stage 3
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TR 33.834** (Rel-16) — Long Term Key Update Procedures Study
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.144** (Rel-19) — UE OTA Antenna Performance Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [OTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ota/)
