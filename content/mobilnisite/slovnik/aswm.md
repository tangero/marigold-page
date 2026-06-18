---
slug: "aswm"
url: "/mobilnisite/slovnik/aswm/"
type: "slovnik"
title: "ASWM – Automated Software Management"
date: 2025-01-01
abbr: "ASWM"
fullName: "Automated Software Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/aswm/"
summary: "ASWM je 3GPP řídicí rámec pro automatizaci životního cyklu softwaru síťových prvků. Umožňuje vzdálené a standardizované nasazení, aktivaci a vrácení softwaru, čímž snižuje provozní náklady a minimaliz"
---

ASWM je 3GPP řídicí rámec pro automatizaci životního cyklu softwaru síťových prvků, umožňující vzdálené a standardizované nasazení, aktivaci a vrácení softwaru.

## Popis

Automated Software Management (ASWM, automatizovaná správa softwaru) je komplexní rámec definovaný v rámci standardů 3GPP, konkrétně v doméně Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)). Jeho primární funkcí je automatizace komplexní správy životního cyklu softwaru na síťových prvcích, jako jsou základnové stanice (eNodeB/gNB), funkce jádra sítě a uživatelská zařízení (v určitých kontextech). Architektura je založena na modelu manažer-agent, kde centralizovaný Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management System ([EMS](/mobilnisite/slovnik/ems/)) funguje jako manažer, vydávající standardizované příkazy agentům správy softwaru umístěným na cílových síťových prvcích. Tyto příkazy jsou přenášeny přes standardizovaná rozhraní, jako jsou ta definovaná pro Itf-N nebo jiná severozápadní rozhraní, s využitím protokolů jako File Transfer Protocol ([FTP](/mobilnisite/slovnik/ftp/)), Trivial File Transfer Protocol ([TFTP](/mobilnisite/slovnik/tftp/)) nebo bezpečnějších alternativ pro doručování softwarových balíčků.

Proces ASWM zahrnuje několik klíčových fází: příprava softwaru, distribuce, aktivace a návrat. Ve fázi přípravy manažer ověří softwarový balíček, který obsahuje spustitelný kód, konfigurační data a manifesty popisující závislosti a kompatibilitu. Distribuční fáze zahrnuje zabezpečený přenos tohoto balíčku z úložiště softwaru do paměťového úložiště cílového síťového prvku. Fáze aktivace je kritickým krokem, kdy je nový software načten do operační paměti síťového prvku, často vyžadující řízený restart. ASWM poskytuje mechanismy pro okamžitou i naplánovanou aktivaci, stejně jako operace commit pro trvalé provedení změny. Základním kamenem ASWM je jeho robustní schopnost návratu (fallback nebo rollback). Pokud nový software neprojde kontrolou integrity, způsobí provozní chyby nebo zhorší výkon, systém může automaticky nebo manuálně přejít zpět na dříve známou stabilní verzi softwaru, čímž zajišťuje kontinuitu síťových služeb.

Klíčové komponenty v rámci ASWM zahrnují Software Management Function v manažeru, Software Management Agent na síťovém prvku a Software Inventory, který sleduje všechny verze softwaru a jejich stavy (např. nainstalovaný, aktivní, potvrzený). Rámec také definuje podrobné stavové modely pro softwarové položky a jejich přidružené spustitelné jednotky, což umožňuje řídicímu systému přesně sledovat životní cyklus každé softwarové komponenty. Role ASWM je nedílnou součástí moderního provozu sítí, umožňuje zero-touch provisioning, bezproblémové aktualizace softwaru pro zavádění nových funkcí nebo bezpečnostních záplat a konzistentní správu napříč více-dodavatelskými prostředími. Tvoří základní část širších iniciativ Self-Organizing Network ([SON](/mobilnisite/slovnik/son/)) a síťové automatizace, snižuje potřebu manuálního zásahu, minimalizuje lidskou chybu a urychluje nasazování nových služeb.

## K čemu slouží

ASWM byl vytvořen, aby řešil významné provozní výzvy a náklady spojené s manuální správou softwaru na tisících distribuovaných síťových prvcích v mobilní síti. Před jeho standardizací byly softwarové aktualizace často proprietární pro konkrétního dodavatele, vyžadovaly návštěvy techniků na místě a nesly vysoké riziko narušení služeb kvůli lidské chybě nebo nekompatibilním verzím. Tento manuální přístup byl neudržitelný s růstem sítí v měřítku a složitosti, zejména se zavedením LTE v Release 8, které slibovalo vyšší přenosové rychlosti a nižší latenci, ale také zvýšilo počet síťových uzlů a frekvenci softwarových aktualizací potřebných pro optimalizaci a nové funkce.

Primární motivací bylo umožnit vzdálenou, automatizovanou a standardizovanou správu životního cyklu softwaru. Tato automatizace řeší kritické problémy: drasticky snižuje provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)) eliminací cest techniků, minimalizuje výpadky sítě během aktualizací prostřednictvím koordinovaných a ověřených procedur a zvyšuje spolehlivost sítě zajištěním konzistence softwaru a umožněním rychlého návratu v případě selhání. Dále ASWM poskytuje společný jazyk a proceduru pro správu softwaru, což je zásadní pro operátory nasazující více-dodavatelské sítě. Bez takového standardu by integrace a správa zařízení od různých dodavatelů byla vysoce neefektivní a náchylná k chybám.

Historicky byl vývoj ASWM v Release 8 součástí širšího úsilí v rámci 3GPP definovat robustní [OAM](/mobilnisite/slovnik/oam/) schopnosti pro novou System Architecture Evolution (SAE) a LTE rádiový přístup. Řešil omezení ad-hoc a proprietárních řídicích řešení používaných v sítích 2G a 3G. Formalizací procesu správy softwaru 3GPP umožnilo operátorům dosáhnout větší agility, bezpečnosti (prostřednictvím včasného nasazování záplat) a provozní efektivity, což je základním předpokladem pro vývoj směrem k plně automatizovaným a programovatelným sítím 5G a budoucím generacím.

## Klíčové vlastnosti

- Standardizovaný formát softwarového balíčku a manifest pro kompatibilitu více dodavatelů
- Vzdálená distribuce a aktivace softwarových obrazů na síťové prvky
- Automatizované procedury pro návrat a přechod zpět na známý stabilní stav
- Podpora naplánované, okamžité a podmíněné aktivace softwaru
- Komplexní správa inventáře softwaru sledující všechny verze a stavy
- Integrace se správou chyb a výkonu pro ověření stavu po aktualizaci

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)

## Definující specifikace

- **TS 32.531** (Rel-19) — 3GPP TS 32.531: SW Management Concepts & IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [ASWM na 3GPP Explorer](https://3gpp-explorer.com/glossary/aswm/)
