---
slug: "cltm"
url: "/mobilnisite/slovnik/cltm/"
type: "slovnik"
title: "CLTM – Conditional L1/L2 Triggered Mobility"
date: 2025-01-01
abbr: "CLTM"
fullName: "Conditional L1/L2 Triggered Mobility"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cltm/"
summary: "Conditional L1/L2 Triggered Mobility (CLTM) je vylepšení mobility pro 5G NR zavedené v Release 19. Umožňuje rychlejší a spolehlivější předávání spojení tím, že umožňuje uživatelskému zařízení (UE) aut"
---

CLTM je vylepšení mobility pro 5G NR od Release 19, které umožňuje rychlejší a spolehlivější předávání spojení tím, že umožňuje uživatelskému zařízení (UE) autonomně provést předem nakonfigurované předání na základě měření z fyzické vrstvy (L1) a vrstvy MAC (L2) v reálném čase.

## Popis

Conditional [L1](/mobilnisite/slovnik/l1/)/[L2](/mobilnisite/slovnik/l2/) Triggered Mobility (CLTM) je sofistikovaný mechanismus předávání spojení navržený k radikálnímu snížení přerušení při změně buňky v 5G New Radio (NR). Na rozdíl od tradičních předání spojení, která jsou plně řízena sítí prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) (proces zahrnující hlášení měření, rozhodnutí o předání a příkazy k předání), CLTM deleguje konečné rozhodnutí o provedení na uživatelské zařízení (UE). Síť předem nakonfiguruje UE se seznamem kandidátských cílových buněk a specifickými spouštěcími podmínkami. Tyto podmínky jsou založeny na rychlých měřeních na konkrétních vrstvách. Podmínky na vrstvě 1 (L1) typicky zahrnují okamžitá měření referenčního signálu přijímaného výkonu (RSRP) nebo kvality (RSRQ) z obsluhující a sousedních buněk. Podmínky na vrstvě 2 (L2) mohou zahrnovat metriky jako stav vyrovnávací paměti nebo indikátory kvality kanálu zpracovávané na vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). UE tyto předem nakonfigurované podmínky kontinuálně monitoruje. Jakmile je splněna spouštěcí podmínka – například, když kvalita signálu z kandidátské buňky překročí kvalitu signálu z obsluhující buňky o určitou mez po stanovenou dobu – může UE autonomně zahájit předání spojení do této předem schválené cílové buňky bez čekání na explicitní příkaz RRC Handover Command ze sítě.

Architektura pro CLTM zahrnuje úzkou koordinaci mezi vrstvami Radio Resource Control (RRC), Packet Data Convergence Protocol (PDCP), Radio Link Control (RLC), MAC a Physical (PHY) v gNB a jejich protějšky v UE. Obsluhující gNB poskytuje konfiguraci CLTM prostřednictvím zprávy RRC Reconfiguration. Tato konfigurace je klíčovou součástí a zahrnuje seznam kandidátských cílových buněk, každou s přidruženými parametry specifickými pro buňku (jako je fyzické ID buňky a kmitočet nosné), a přesné spouštěcí podmínky L1/L2 s příslušnými prahy. Konfigurace může také zahrnovat prováděcí podmínky, což jsou další kritéria, která musí být splněna před dokončením předání, což zajišťuje robustnost přesunu. UE tuto konfiguraci uloží a aktivuje proceduru vyhodnocování podmíněného předání.

Když UE zjistí, že jsou splněny spouštěcí a prováděcí podmínky pro konkrétní kandidátskou buňku, provede synchronní proceduru náhodného přístupu k cílové buňce. Klíčovým prvkem je zařazení 'indikace CLTM' do Zprávy 1 (Preambule náhodného přístupu) nebo Zprávy 3 (RRC Reconfiguration Complete) této procedury. Tato indikace informuje cílový gNB, že se jedná o předání spuštěné CLTM, což mu umožní efektivně získat kontext UE ze zdrojového gNB (přes rozhraní Xn) a připravit prostředky. Celý proces, od splnění podmínek k úspěšnému připojení k cílové buňce, proběhne s minimální signalizační latencí, protože časově náročný cyklus příkazů a odpovědí RRC mezi obsluhujícím gNB a UE je pro fázi provedení eliminován.

Úlohou CLTM v síti je zvýšit robustnost a výkon mobility, zejména v náročných rádiových prostředích. Jedná se o základní technologii pro umožnění plynulé mobility ve vysokých kmitočtových pásmech (jako je mmWave), která jsou náchylná k rychlému zhoršování signálu, a ve scénářích s vysokou rychlostí (např. komunikace vozidel). Snížením doby přerušení při předání spojení CLTM přímo přispívá k naplnění přísných požadavků na spolehlivost a zpoždění pokročilých případů užití 5G-Advanced a budoucího 6G, jako je průmyslová automatizace, autonomní vozidla a rozšířená realita (XR). Představuje posun od síťově centrického k více uživatelským zařízením asistovanému řízení mobility, čímž zvyšuje celkovou obratnost a rychlou reakci rádiové přístupové sítě.

## K čemu slouží

CLTM bylo vytvořeno k řešení základních omezení latence a spolehlivosti konvenčních předání spojení řízených [RRC](/mobilnisite/slovnik/rrc/) v 5G NR. Jak se sítě 5G vyvíjely, aby podporovaly aplikace s kritickými požadavky na spolehlivost pod hlavičkou URLLC, doba přerušení při předání spojení v řádu desítek milisekund v původních procedurách se stala významným omezením. Tato latence, způsobená potřebou hlášení měření, síťového zpracování a přenosu příkazů RRC, mohla vést ke ztrátě paketů, přerušení spojení a zhoršení kvality služeb v dynamickém prostředí. Primární problém, který CLTM řeší, je toto signalizační zpoždění během kritické prováděcí fáze předání spojení.

Historicky bylo Conditional Handover ([CHO](/mobilnisite/slovnik/cho/)), zavedené v dřívějších releasech, krokem vpřed díky přípravě předání spojení předem. CHO však stále spoléhalo na spouštěče a signalizaci na vrstvě RRC. CLTM tento koncept posouvá dále využitím rychlejších spouštěčů na nižších vrstvách ([L1](/mobilnisite/slovnik/l1/)/[L2](/mobilnisite/slovnik/l2/)). Motivace vychází z potřeby mobility s 'nulovým' nebo 'téměř nulovým' přerušením, zejména pro případy užití zahrnující vysokou mobilitu nebo přenosy přes nestabilní vysokofrekvenční kanály. V takových scénářích se mohou rádiové podmínky změnit během milisekund a čekání na příkaz RRC od potenciálně degradovaného obsluhujícího spoje je riskantní. CLTM umožňuje UE jednat okamžitě na základě aktuálních rádiových podmínek a předcházet tak selhání spoje.

CLTM dále řeší omezení předchozích procedur správy paprsků a předání spojení mezi buňkami v hustých sítích. Poskytuje jednotnější a efektivnější rámec pro řízení událostí mobility, které jsou nejlépe detekovatelné na fyzické vrstvě, jako je náhlé zastínění paprsku nebo objevení se silnějšího paprsku ze sousední buňky. Vytvořením standardizovaného mechanismu pro mobilitu spouštěnou na L1/L2 umožňuje 3GPP konzistentní implementaci a interoperabilitu, což přesahuje rámec specifických rychlých schémat předání spojení jednotlivých dodavatelů. Jeho zavedení v Release 19 je klíčovým milníkem na cestě k 5G-Advanced, který zvyšuje schopnost systému podporovat skutečně plynulé připojení.

## Klíčové vlastnosti

- Autonomní provedení předání spojení spuštěné uživatelským zařízením (UE) na základě předem nakonfigurovaných síťových podmínek
- Využití rychlých spouštěčů založených na měřeních vrstvy 1 (např. RSRP/RSRQ) a vrstvy 2 (např. metriky MAC)
- Předkonfigurace kandidátských cílových buněk a spouštěcích/prováděcích podmínek prostřednictvím signalizace RRC
- Snížení doby přerušení při předání spojení eliminací latence příkazu RRC pro fázi provedení
- Zvýšená robustnost mobility ve scénářích s vysokou rychlostí a ve vysokých kmitočtových pásmech (např. mmWave)
- Podpora synchronního náhodného přístupu s indikací CLTM k cílové buňce pro efektivní získání kontextu

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CLTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cltm/)
