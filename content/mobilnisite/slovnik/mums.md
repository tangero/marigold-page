---
slug: "mums"
url: "/mobilnisite/slovnik/mums/"
type: "slovnik"
title: "MUMS – Multi User Mobile Station"
date: 2025-01-01
abbr: "MUMS"
fullName: "Multi User Mobile Station"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mums/"
summary: "MUMS označuje mobilní stanici schopnou současně podporovat více uživatelů, například ve vozidle nebo ve scénáři se sdíleným zařízením. Umožňuje sdílení prostředků a efektivní konektivitu pro skupiny,"
---

MUMS je mobilní stanice podporující více uživatelů současně, což umožňuje sdílení prostředků a efektivní skupinovou konektivitu ve scénářích jako jsou sdílená vozidla nebo zařízení.

## Popis

Multi User Mobile Station (MUMS) je koncept ve standardech 3GPP, zavedený ve vydání 5, který popisuje mobilní stanici obsluhující více koncových uživatelů současně. Na rozdíl od tradičních mobilních stanic navržených pro jednotlivé uživatele funguje MUMS jako sdílený přístupový bod nebo brána, umožňující více uživatelům nebo zařízením připojit se k síti prostřednictvím jediného mobilního rozhraní. Architektonicky může být MUMS implementována v různých formách, například jako zařízení ve vozidle poskytující konektivitu pasažérům, sdílený hotspot nebo IoT brána agregující data z více senzorů. Zahrnuje komponenty jako rádiový transceiver, síťové rozhraní a modul správy uživatelů pro zvládnutí více datových relací a identit.

Fungování MUMS zahrnuje správu více předplatitelských identit nebo relací přes jediné rádiové připojení. V raných vydáních 3GPP byl tento koncept často konceptualizován pro scénáře jako mobilní kanceláře nebo veřejné přístupové body, kde se MUMS autentizovala v síti a následně distribuovala konektivitu připojeným uživatelům. Mobilní stanice může používat techniky jako překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)) nebo tunelování k oddělení provozu různých uživatelů. Mezi klíčové funkce patří správa relací, upřednostňování kvality služeb (QoS) pro více datových proudů a zajištění zabezpečení pro ochranu dat každého uživatele. V síti MUMS interaguje s prvky jádra sítě, jako jsou [SGSN](/mobilnisite/slovnik/sgsn/) a GGSN v systémech [GPRS](/mobilnisite/slovnik/gprs/)/UMTS, registruje se jako jediná entita a zároveň podporuje více datových toků.

V průběhu času se koncept MUMS vyvinul, aby odpovídal moderním případům užití, jako je skupinová komunikace v LTE a 5G, brány pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) pro IoT a systémy komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)). Hraje roli při efektivním využívání prostředků tím, že snižuje režii síťové signalizace agregací připojení. Například v IoT nasazení může brána typu MUMS shromažďovat data z mnoha senzorů a přenášet je periodicky, čímž šetří energii a spektrum. Ačkoli se termín 'MUMS' v posledních vydáních používá méně často, jeho principy jsou základem technologií jako je skupinová komunikace [ProSe](/mobilnisite/slovnik/prose/) (Proximity Services) a síťové segmentování (network slicing) pro více nájemců.

## K čemu slouží

MUMS byl zaveden ve vydání 3GPP 5, aby řešil potřebu sdílené mobilní konektivity v nově se objevujících scénářích, jako je komunikace ve vozidlech, podniková prostředí a veřejné přístupové body. Před MUMS se mobilní sítě primárně zaměřovaly na zařízení pro jednoho uživatele, což omezovalo efektivitu ve skupinových prostředích. Růst využívání mobilních dat a nástup služeb 3G vytvořil poptávku po stanicích, které by mohly podporovat více uživatelů, čímž by se snížily náklady a požadavky na infrastrukturu pro scénáře, kde byla individuální zařízení nepraktická.

Vytvoření MUMS bylo motivováno omezeními dřívějších mobilních systémů, kterým chyběly standardizované mechanismy pro podporu více uživatelů. Historické přístupy spoléhaly na ad-hoc řešení nebo externí směrovací zařízení, což vedlo k problémům s interoperabilitou a bezpečnostními slabinami. MUMS poskytl rámec v rámci standardů 3GPP pro definici toho, jak může mobilní stanice zvládat více uživatelů, a řešil tak problémy jako současná správa relací a přidělování síťových prostředků. Umožnil případy užití, jako je internetový přístup ve vozidle, sdílené mobilní hotspoty a raná agregace IoT, čímž připravil cestu pro pozdější pokroky ve skupinové komunikaci a masivním IoT. Tím byla řešena potřeba škálovatelné a efektivní konektivity v kolaborativních nebo hustě obydlených uživatelských prostředích.

## Klíčové vlastnosti

- Podporuje více uživatelů nebo zařízení prostřednictvím jediné mobilní stanice
- Umožňuje sdílenou konektivitu ve vozidlech, hotech nebo IoT branách
- Spravuje více datových relací a předplatitelských identit
- Zahrnuje upřednostňování QoS pro různorodý uživatelský provoz
- Snižuje síťovou signalizaci agregací připojení
- Evoluční základ pro skupinovou komunikaci a agregaci IoT

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MUMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mums/)
