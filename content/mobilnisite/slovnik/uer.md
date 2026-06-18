---
slug: "uer"
url: "/mobilnisite/slovnik/uer/"
type: "slovnik"
title: "UER – User Equipment with ODMA relay operation enabled"
date: 2025-01-01
abbr: "UER"
fullName: "User Equipment with ODMA relay operation enabled"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uer/"
summary: "UER označuje User Equipment schopné fungovat jako přenosový uzel (relay node) v síti s přístupem řízeným příležitostí (Opportunity Driven Multiple Access - ODMA). Může přijímat a znovu vysílat signály"
---

UER je User Equipment schopné fungovat jako ODMA přenosový uzel (relay) pro rozšíření pokrytí sítě přijímáním a opětovným vysíláním signálů mezi vzdáleným UE a základnovou stanicí.

## Popis

User Equipment s povolenou [ODMA](/mobilnisite/slovnik/odma/) přenosovou funkcí (UER) je UE, které obsahuje funkcionalitu definovanou protokolem přístupu řízeného příležitostí (Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/) - ODMA). ODMA byl koncept zkoumaný v raných vydáních 3GPP (především pro UMTS) jako metoda pro více-skokovou komunikaci. Zařízení UER může pracovat ve dvou režimech: jako standardní terminál komunikující přímo s Node B (základnovou stanicí), nebo jako přenosový uzel (relay). V přenosovém režimu vyhledává další UE, navazuje ad-hoc spojení a přeposílá jejich provoz směrem k síťové infrastruktuře.

Protokol ODMA, specifikovaný v dokumentech jako TS 25.301 a 25.321, definuje vrstvenou strukturu pro tuto činnost. Zahrnuje mechanismy pro zjišťování sousedních uzlů, vytváření a udržování cest v rámci ad-hoc přenosové sítě. UER skenuje další zařízení s podporou ODMA, měří kvalitu spojení a účastní se distribuovaných směrovacích algoritmů pro nalezení efektivních více-skokových cest zpět k Node B. Přeposílání mohlo probíhat na fyzické vrstvě nebo zahrnovat přeposílání paketů na síťové vrstvě, v závislosti na architektuře. UER spravuje své vlastní zdroje, vyvažuje svou roli přenosového uzlu pro ostatní se svou primární funkcí jako zařízení účastníka.

Z pohledu sítě se UER jeví jako rozšíření rádiové přístupové sítě (RAN). Vytváří dynamickou, samoorganizující se síť typu mesh mezi terminály. To vyžaduje specifické protokoly pro zabezpečení (aby se zabránilo zneužití přenosových uzlů), přidělování zdrojů (pro správu baterie UER a rušení) a správu mobility (s ohledem na měnící se ad-hoc topologii). Jádrová síť si může být přenosu vědoma, ale obvykle zachází s koncovým spojením jako s jediným přenosovým kanálem (bearer) končícím u vzdáleného UE. Koncept UER byl předchůdcem později standardizovaných přenosových technologií, jako jsou LTE Relay Nodes a 5G Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)).

## K čemu slouží

Koncept UER byl vyvinut pro řešení klíčových výzev při raném nasazování sítí 3G: děr v pokrytí a omezení kapacity, zejména na okrajích buněk nebo v náročných rádiových prostředích, jako jsou vnitřní prostory nebo venkovské oblasti. Nasazení dalších základnových stanic je nákladné a časově náročné. [ODMA](/mobilnisite/slovnik/odma/) a UER nabízely potenciální řešení využitím existující populace uživatelských zařízení k vytvoření virtuální, více-skokové infrastruktury, která by decentralizovaným a nákladově efektivním způsobem rozšířila pokrytí.

Cílem bylo vyřešit problém 'poslední míle' v bezdrátových sítích využitím blízkých zařízení jako spontánních přenosových uzlů. To mohlo zlepšit parametry spojení (link budget) pro vzdálená UE rozdělením dlouhého spojení s nízkou kvalitou na několik kratších skoků s vyšší kvalitou. Dále slibovalo zvýšení celkové kapacity sítě umožněním prostorového opakovaného využití spektra v rámci buňky prostřednictvím ad-hoc sítě typu mesh. To bylo zvláště atraktivní pro datové služby v UMTS, kde byla kapacita klíčovým problémem.

Motivace vycházela z výzkumu ad-hoc sítí a vojenských MANETs (Mobile Ad-hoc Networks). 3GPP to studovalo jako způsob, jak vylepšit možnosti UMTS. Složitost implementace – včetně výrazného vybíjení baterie přenosového zařízení, sofistikovaných směrovacích protokolů, bezpečnostních rizik a správy rušení – se však ukázala jako hlavní překážka. Přestože byly ODMA a UER standardizovány, došlo k jejich omezenému komerčnímu nasazení. Jejich principy však ovlivnily pozdější práce o komunikaci typu zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)) v LTE [ProSe](/mobilnisite/slovnik/prose/) a sofistikované přenosové architektury v 5G.

## Klíčové vlastnosti

- Dvojrežimový provoz jako standardní UE a přenosový uzel (relay node)
- Implementace zásobníku protokolů ODMA pro ad-hoc směrování
- Schopnost zjišťování sousedních uzlů a dynamického vytváření cest
- Funkcionalita pro přeposílání paketů na fyzické nebo síťové vrstvě
- Cílí na rozšíření pokrytí sítě a zlepšení kapacity
- Funguje jako součást samoorganizující se mobilní ad-hoc sítě

## Související pojmy

- [ODMA – Opportunity Driven Multiple Access](/mobilnisite/slovnik/odma/)
- [D2D – Device-to-Device](/mobilnisite/slovnik/d2d/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [UER na 3GPP Explorer](https://3gpp-explorer.com/glossary/uer/)
