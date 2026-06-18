---
slug: "irat"
url: "/mobilnisite/slovnik/irat/"
type: "slovnik"
title: "IRAT – Inter-Radio Access Technology"
date: 2025-01-01
abbr: "IRAT"
fullName: "Inter-Radio Access Technology"
category: "Mobility"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/irat/"
summary: "Inter-RAT (IRAT) označuje mobilitu a interakci mezi různými generacemi nebo typy rádiových přístupových sítí (RAN) v rámci systému 3GPP nebo mezi sítěmi 3GPP a ne-3GPP. Umožňuje plynulé předávání hovo"
---

IRAT je 3GPP termín pro mobilitu a interakci mezi různými typy rádiových přístupových sítí, umožňující předávání hovorů a správu konektivity napříč heterogenními technologiemi, jako jsou sítě 3GPP a ne-3GPP.

## Popis

Inter-RAT zahrnuje procedury, protokoly a síťové schopnosti, které umožňují uživatelskému zařízení (UE) přecházet mezi různými rádiovými přístupovými technologiemi. Mezi běžné příklady patří mobilita mezi LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a [WCDMA](/mobilnisite/slovnik/wcdma/)/[HSPA](/mobilnisite/slovnik/hspa/) ([UTRAN](/mobilnisite/slovnik/utran/)), mezi 5G NR a LTE nebo mezi sítí 3GPP (např. 5G) a sítí ne-3GPP (např. Wi-Fi). Architektura pro IRAT mobilitu zahrnuje koordinaci mezi jádrem sítě (např. 5GC, EPC) a různými RAN. Mezi klíčové síťové uzly patří zdrojová a cílová základnová stanice (např. gNB, [eNB](/mobilnisite/slovnik/enb/), NodeB) a řídicí funkce roviny řízení v jádru sítě, jako jsou [AMF](/mobilnisite/slovnik/amf/)/[SMF](/mobilnisite/slovnik/smf/) v 5GC nebo [MME](/mobilnisite/slovnik/mme/) v EPC, které spravují kontext relace a mobility.

Fungování IRAT zahrnuje několik klíčových procedur. První je IRAT měření, při kterém UE, nakonfigurované sítí, měří kvalitu signálu sousedních buněk na jiné RAT. Síť pro tato měření poskytuje měřicí mezery – krátká období, kdy UE přelaďuje svůj přijímač od obsluhující buňky. Na základě měřicích reportů od UE se síť rozhodne iniciovat IRAT předání hovoru. Jádro sítě řídí předání přípravou prostředků v cílové RAT, přenosem kontextu UE (včetně bezpečnostního kontextu a QoS toků) a vydáním příkazu UE k přepnutí. U paketově orientovaných služeb to zahrnuje přesměrování datových paketů ze zdrojového do cílového systému pro minimalizaci ztrát. V případě mobility v klidovém režimu umožňují procedury IRAT překládání buněk, aby si UE autonomně vybrala vhodnou buňku na jiné RAT na základě vysílaných parametrů a vlastních měření.

IRAT rovněž pokrývá scénáře pro vzájemnou spolupráci přesahující jednoduché předávání hovorů, jako je současná konektivita přes více RAT (např. agregace LTE-WLAN v Rel-13) nebo směrování, přepínání a rozdělování přístupového provozu mezi přístupy 3GPP a ne-3GPP v 5G (ATSSS). Role IRAT je zásadní pro poskytování nepřetržitého pokrytí službami a využití nejlepšího dostupného síťového zdroje. Umožňuje operátorům efektivně spravovat jejich nasazení více RAN, vykládat provoz a zajišťovat uživatelům udržení konektivity při pohybu z pokrytí jedné technologie do druhé, což je klíčové pro kontinuitu hlasových a datových služeb.

## K čemu slouží

IRAT technologie existuje, aby řešila zásadní problém poskytování plynulé mobility a kontinuity služeb ve světě s více koexistujícími rádiovými přístupovými technologiemi. Žádná jednotlivá RAT neposkytuje univerzální pokrytí ani optimální výkon pro všechny služby a lokality. Sítě 2G/3G, 4G LTE, 5G NR a Wi-Fi jsou často nasazeny ve vrstvách s překryvem. Účelem IRAT procedur je umožnit mobilnímu zařízení pohyb mezi těmito technologiemi bez přerušení aktivních relací (jako je hovor nebo video stream) a efektivně spravovat jeho konektivitu v klidovém režimu.

Historicky, s uvedením nových generací (např. 3G UMTS, poté 4G LTE), potřebovali operátoři migrační cestu. Rané systémy měly omezené nebo neohrabané mezi-RAT schopnosti. Standardizované IRAT procedury předávání hovorů a překládání buněk, významně vylepšené v 3GPP Rel-8 se zavedením LTE, byly motivovány potřebou hladkého vývoje sítě a konzistentního uživatelského zážitku. Řešily omezení, kdy zařízení ztrácela konektivitu při opuštění pokrytí novější technologie, což nutilo k manuálnímu opětovnému připojení nebo k rušivému přerušení a znovunavázání relací.

IRAT řeší kritické provozní problémy a problémy uživatelského zážitku. Umožňuje operátorům přeorganizovat spektrum (např. přesun spektra z 3G do 4G/5G) při zachování pokrytí díky přechodu na starší technologie. Umožňuje vyrovnávání zatížení a směrování provozu mezi RAT pro optimalizaci využití síťových zdrojů. Pro uživatele poskytuje vnímání jedné, vždy nejlépe připojené sítě, i když se podkladová technologie během cesty může změnit mnohokrát. V 5G, s důrazem na integraci s ne-3GPP, jsou principy IRAT rozšířeny, aby umožnily bezpečnou, plynulou mobilitu mezi NR a důvěryhodnými/nedůvěryhodnými Wi-Fi sítěmi, což je nezbytné pro naplnění slibu 5G o všudypřítomné, vysoce výkonné konektivitě.

## Klíčové vlastnosti

- Podporuje předávání aktivních UE mezi různými RAT (např. NR na LTE, LTE na WCDMA)
- Definuje měřicí procedury a mezery pro vyhodnocování sousedních RAT buněk UE
- Umožňuje překládání buněk v klidovém režimu napříč RAT na základě priority a síly signálu
- Umožňuje přenos bezpečnostního kontextu a QoS parametrů při změně RAT
- Podporuje přesměrování dat mezi systémy pro minimalizaci ztráty paketů během předání
- Rozšiřuje se na vzájemnou spolupráci s přístupy ne-3GPP, jako je Wi-Fi, v pozdějších vydáních

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 32.642** (Rel-11) — UTRAN Network Resource Model for Configuration Management
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [IRAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/irat/)
