---
slug: "nt"
url: "/mobilnisite/slovnik/nt/"
type: "slovnik"
title: "NT – Network Termination"
date: 2025-01-01
abbr: "NT"
fullName: "Network Termination"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nt/"
summary: "Funkční skupina nebo fyzické zařízení představující rozhraní mezi uživatelským koncovým zařízením a veřejnou telekomunikační sítí. Přizpůsobuje uživatelské signály pro přenos po síti a je standardním"
---

NT je funkční skupina nebo zařízení na rozhraní mezi uživatelským koncovým zařízením a veřejnou sítí, které přizpůsobuje uživatelské signály pro přenos a slouží jako standardní referenční bod rozhraní.

## Popis

Síťové ukončení (NT) je základní koncept v architektuře telekomunikačních sítí označující demarkační bod mezi uživatelským koncovým zařízením ([CPE](/mobilnisite/slovnik/cpe/)) a veřejnou sítí operátora. Jedná se o funkční skupinu, často realizovanou jako fyzické zařízení (např. modem nebo optický síťový terminál), která ukončuje přenosovou linku na straně sítě a poskytuje standardizované rozhraní pro připojení uživatelského zařízení. NT vykonává základní adaptační funkce, které zahrnují řádkové kódování, obnovu časování, rámování a elektrickou či optickou převod signálu, aby se uživatelská data stala kompatibilní s transportní technologií přístupové sítě (např. [DSL](/mobilnisite/slovnik/dsl/), optické [PON](/mobilnisite/slovnik/pon/) nebo [ISDN](/mobilnisite/slovnik/isdn/)). V protokolových zásobnících je NT klíčovým referenčním bodem (často označovaným jako referenční body T, S nebo U v modelech ISDN/[B-ISDN](/mobilnisite/slovnik/b-isdn/)), který jasně odděluje odpovědnosti uživatele ([TE](/mobilnisite/slovnik/te/) – koncové zařízení) a sítě ([LT](/mobilnisite/slovnik/lt/) – ukončení linky na ústředně).

V detailním provozu NT funguje jako aktivní prostředník. Na straně sítě komunikuje s vybavením pro ukončení linky (LT) umístěným v centrále operátora nebo v uliční skříni pomocí protokolů specifických pro danou přístupovou technologii (např. G.hn pro DSL, [GPON](/mobilnisite/slovnik/gpon/) pro optiku). Na uživatelské straně poskytuje jedno nebo více standardizovaných rozhraní, jako je Ethernetový port, port pro analogovou telefonii (POTS) nebo rozhraní sběrnice ISDN S/T. Například při nasazení technologie Fiber-to-the-Home (FTTH) je optický síťový terminál (ONT) tímto NT. Přijímá optické signály ze sítě, převádí je na elektrické Ethernetové rámce a často poskytuje funkce směrování, Wi-Fi a VoIP adaptéru pro domácnost. Jeho klíčová role spočívá v izolaci složitosti přístupové sítě od uživatelských zařízení.

Z architektonického hlediska je NT kritickou komponentou pro definici jasných hranic sítě, což je zásadní pro interoperabilitu, testování, izolaci závad a regulatorní shodu. Zajišťuje, že jakékoli standardům odpovídající uživatelské zařízení se může k síti připojit, pokud používá správné rozhraní na NT. V kontextech 3GPP, ačkoli se o něm diskutuje méně často než v pevných sítích, se tento koncept objevuje ve specifikacích týkajících se konvergence pevných a mobilních sítí, přenosových tras a při definování rozhraní pro integrovaný přístup a přenosovou trasu (IAB) nebo síťové přípojné body. NT představuje „poslední zařízení ve vlastnictví sítě“ před vstupem do uživatelské domény, což z něj činí klíčový bod pro aktivaci služeb, vynucování kvality služeb a správu sítě.

## K čemu slouží

Koncept síťového ukončení existuje za účelem vytvoření jasné, standardizované hranice mezi sítí poskytovatele služeb a soukromou doménou zákazníka. To řeší několik kritických problémů: definuje odpovědnost za údržbu (operátor spravuje síť až k NT), zajišťuje interoperabilitu mezi CPE a síťovým vybavením různých výrobců a poskytuje stabilní bod rozhraní pro připojení široké škály uživatelských terminálů. Historicky, bez standardizovaného NT, byly sítě proprietární, což uzamykalo zákazníky do specifického vybavení od jejich poskytovatele a ztěžovalo diagnostiku závad.

Ve vývoji telekomunikačních sítí, od analogové telefonie přes ISDN a DSL až po dnešní optiku, bylo NT konstantním architektonickým kotvištěm. Jeho účel se rozšířil od jednoduchého elektrického ukončení v ISDN až k zahrnutí složitých funkcí, jako je převod protokolů, označování QoS a dokonce směrování v moderních zařízeních. Pro 3GPP, které se primárně zaměřuje na rádiové a core sítě, je koncept NT relevantní ve specifikacích zabývajících se integrací pevných sítí, například při definování, jak se síťové funkce 5G připojují k pevnému přístupu pro přenosové trasy, nebo jak rezidenční brány (které často zahrnují funkci NT) komunikují s 5G Core pro pevný bezdrátový přístup. Řeší základní potřebu čistého oddělení síťové kontroly od uživatelského zařízení, což umožňuje škálovatelné, spravovatelné a vícevýrobcové přístupové sítě.

## Klíčové vlastnosti

- Demarkační bod mezi veřejnou sítí a zákaznickou přípojkou
- Provádí adaptaci signálu (řádkové kódování, rámování, převod) pro síťový transport
- Poskytuje standardizovaná uživatelsko-síťová rozhraní (např. Ethernet, POTS, ISDN S/T)
- Často implementováno jako fyzické zařízení (např. modem, ONT, NT1)
- Umožňuje izolaci závad a jasné hranice provozní odpovědnosti
- Klíčový referenční bod v modelech síťové architektury (např. referenční body ISDN)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks

---

📖 **Anglický originál a plná specifikace:** [NT na 3GPP Explorer](https://3gpp-explorer.com/glossary/nt/)
