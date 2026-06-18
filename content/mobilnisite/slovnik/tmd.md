---
slug: "tmd"
url: "/mobilnisite/slovnik/tmd/"
type: "slovnik"
title: "TMD – Transparent Mode Data"
date: 2025-01-01
abbr: "TMD"
fullName: "Transparent Mode Data"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tmd/"
summary: "TMD je služba poskytovaná vrstvou řízení rádiového spoje (RLC) v protokolech 3GPP. Nabízí nepřijímání potvrzení při přenosu dat bez segmentace, opětovného sestavování nebo opakování, čímž poskytuje je"
---

TMD (přenos dat v transparentním režimu) je služba vrstvy řízení rádiového spoje (RLC) pro nepřijímání potvrzení, určená k přenosu dat s nízkou latencí bez segmentace nebo opakování, používaná pro streamování nebo vysílací provoz, kde chyby řeší vyšší vrstvy.

## Popis

Transparent Mode Data (TMD, přenos dat v transparentním režimu) je jedna ze tří služeb přenosu dat (vedle nespolehlivého režimu a spolehlivého režimu) poskytovaných podvrstvou řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) v protokolovém zásobníku 3GPP pro UMTS (TS 25.322), LTE (TS 36.322) a NR (TS 38.322). Při provozu v transparentním režimu ([TM](/mobilnisite/slovnik/tm/)) vrstva RLC poskytuje průchozí službu pro protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) vyšších vrstev. Definující vlastností TMD je, že vrstva RLC na datech neprovádí žádnou manipulaci; nepřidává žádnou hlavičku RLC, neprovádí segmentaci ani konkatenaci a nevykonává žádné procedury opakování nebo opravy chyb.

Architektonicky je služba TMD zřízena mezi protějškovými RLC entity TM, obvykle konfigurovanými pro specifické logické kanály přenášející řídicí informace nebo na zpoždění citlivá uživatelská data. Ve vysílající entitě přijímá RLC servisní datovou jednotku ([SDU](/mobilnisite/slovnik/sdu/)) od vyšší vrstvy (např. od vrstvy konvergenčního protokolu paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) nebo vrstvy [RRC](/mobilnisite/slovnik/rrc/)). U TMD je tato SDU předána přímo nižší vrstvě (vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/))) jako PDU RLC bez jakékoli modifikace. Na přijímací straně entita TM RLC obdrží PDU od vrstvy MAC a předá ji jako SDU vyšší vrstvě, opět bez zpracování. Služba je skutečně transparentní.

Jak funguje, je vnitřně jednoduché, ale pro určité typy provozu klíčové. Protože neexistuje hlavička RLC, nabízí TMD nejnižší možnou režii a minimální procesní zpoždění. Neposkytuje však žádné záruky. Data mohou být ztracena kvůli rádiovým chybám, neboť v rámci RLC není mechanismus automatického opakovaného dotazu ([ARQ](/mobilnisite/slovnik/arq/)). Podobně může dojít k doručení mimo pořadí, pokud nižší vrstvy přeuspořádají pakety. TMD je proto vhodná pouze pro aplikace, kde jsou takové ztráty přijatelné nebo jsou řešeny protokoly aplikační vrstvy, nebo pro informace vysílané periodicky, kde lze ztracený paket ignorovat. Její klíčová úloha v síti spočívá v poskytování efektivního kanálu s nízkou latencí pro časově kritické signalizace (jako některé zprávy RRC vysílané na BCCH) a pro určité typy provozu v uživatelské rovině, jako je Voice over IP (VoIP), kde vyrovnávací paměti dokážou zpracovat určité ztráty, nebo pro služby multimediálního vysílání.

## K čemu slouží

TMD byla zavedena již od nejstarších specifikací RLC 3GPP za účelem naplnění potřeby služby přenosu dat s ultra nízkou latencí a minimální režií v rámci rádiového protokolového zásobníku. Ne všechna data vyžadují robustní záruky doručení v pořadí, které poskytuje spolehlivý režim (AM). Některé typy provozu, zejména signalizace řízení v reálném čase a určité typy streamovaných médií, upřednostňují včasnost před absolutní spolehlivostí.

Problém, který TMD řeší, je vyhnutí se zbytečnému procesnímu zpoždění a režii protokolu pro informace citlivé na zpoždění nebo tolerantní ke ztrátám. Použití AM nebo dokonce nespolehlivého režimu (UM) pro takový provoz by přidalo režii hlaviček a procesní latenci pro segmentaci/opětovné sestavení a číslování sekvencí, což by mohlo degradovat výkon aplikací reálného času. Například systémové informace vysílané buňkou musí být přijaty rychle všemi UE v jejím pokrytí; čekání na opakování ztracených bloků není praktické a informace jsou často opakovány v následných vysíláních.

Její vytvoření a přetrvání napříč 2G, 3G, 4G a 5G odráží základní konstrukční princip ve vrstvených komunikačních protokolech: poskytování více úrovní kvality služeb pro různé požadavky aplikací. TMD představuje co možná 'nejlehčí' službu. Řeší problém efektivní přepravy dat tam, kde náklady mechanismů spolehlivosti (na latenci a režii) převažují nad jejich přínosem. Tento návrh umožňuje síťovým architektům mapovat různé typy logických kanálů na nejvhodnější režim RLC, čímž optimalizuje celkový výkon systému a využití zdrojů pro směs typů provozu.

## Klíčové vlastnosti

- Nulová režie hlavičky RLC, maximalizace spektrální účinnosti pro podporovaný provoz
- Minimální procesní zpoždění, protože se neprovádí segmentace, konkatenace ani opakování
- Vhodné pro na zpoždění citlivou signalizaci a provoz uživatelské roviny v reálném čase
- Žádná záruka doručení v pořadí; pakety mohou být ztraceny nebo doručeny mimo pořadí
- Konfigurováno pro každý logický kanál na základě požadavků QoS přenášených dat
- Zachovává konzistenci napříč specifikacemi RLC protokolů UMTS, LTE a NR

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [TMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmd/)
