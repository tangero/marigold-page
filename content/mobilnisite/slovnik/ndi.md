---
slug: "ndi"
url: "/mobilnisite/slovnik/ndi/"
type: "slovnik"
title: "NDI – Network Digital Interface"
date: 2025-01-01
abbr: "NDI"
fullName: "Network Digital Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ndi/"
summary: "Standardizovaná specifikace digitálního rozhraní pro propojení síťových prvků v mobilních sítích, zejména mezi komponenty rádiového přístupu a jádra sítě. Definuje fyzikální, elektrické a logické char"
---

NDI je standardizovaná specifikace digitálního rozhraní pro propojení síťových prvků, jako jsou komponenty rádiového přístupu a jádra sítě, která definuje fyzikální, elektrické a logické charakteristiky pro přenos.

## Popis

Network Digital Interface (NDI) v 3GPP specifikacích označuje standardizované digitální rozhraní používané pro vzájemné propojení různých síťových prvků nebo podsystémů. Zatímco uvedené specifikace (25.705, 26.805, 38.213, 38.889) pokrývají aspekty RAN a služeb, tento termín se často vztahuje k rozhraní používanému pro přenos základnových digitálních signálů, řídicích informací a synchronizačních dat. V kontextu rádiových přístupových sítí, například ve specifikacích pro IMT-2020 (5G) nebo LTE-Advanced, může být NDI spojováno s interním rozhraním distribuované základnové stanice, jako je rozhraní mezi řídicí jednotkou rádiového zařízení (Radio Equipment Control, [REC](/mobilnisite/slovnik/rec/)) a rádiovým zařízením (Radio Equipment, [RE](/mobilnisite/slovnik/re/)), jak je definováno ve standardech jako CPRI (Common Public Radio Interface) nebo podobných.

Specifikace NDI zahrnuje několik vrstev. Fyzická vrstva definuje médium (např. optické vlákno), konektory, řádkový kód a přenosové rychlosti pro zajištění vysokorychlostního přenosu dat s nízkou latencí. Linková a transportní vrstva definují rámování, synchronizaci a mechanismy pro multiplexování různých datových toků (uživatelská data, signalizace řídicí a managementové roviny, synchronizační informace). Pro rozdělení distribuované jednotky ([DU](/mobilnisite/slovnik/du/)) a rádiové jednotky ([RU](/mobilnisite/slovnik/ru/)) v 5G by NDI přenášelo digitalizované rádiové vzorky (I/Q data) pro více anténních nosných spolu s časováním a řídicími zprávami nezbytnými pro koordinovaný přenos a příjem.

Z pohledu síťové architektury NDI umožňuje funkční dekompozici a fyzické oddělení funkcí základnové stanice. To je klíčové pro architektury Cloud RAN (C-RAN) a Open RAN. Díky standardizovanému digitálnímu rozhraní mohou operátoři kombinovat zařízení od různých dodavatelů pro REC/DU a RE/RU, což podporuje interoperabilitu a inovace. Rozhraní musí podporovat velmi vysoké přenosové rychlosti, aby zvládlo velké množství I/Q dat generovaných širokými šířkami pásma a massive [MIMO](/mobilnisite/slovnik/mimo/), a musí mít extrémně nízkou a deterministickou latenci, aby splnilo požadavky rádiového časování pro funkce jako koordinovaný multipoint (CoMP) a těsná synchronizace [TDD](/mobilnisite/slovnik/tdd/).

## K čemu slouží

Network Digital Interface byl vytvořen, aby řešil výzvy rostoucí složitosti základnových stanic, nákladů a závislosti na jediném dodavateli. Tradiční základnové stanice byly integrované jednotky, kde bylo rádiové a základnové zpracování umístěno společně. To činilo stanice objemnými, obtížně modernizovatelnými a vázalo operátory na proprietární řešení jediného dodavatele pro hardware i software. NDI umožňuje funkční rozdělení, které odděluje základnové zpracování (často výpočetně náročnější a softwarově aktualizovatelné) od rádiových frekvenčních komponent.

Toto oddělení řeší několik klíčových problémů. Umožňuje centralizované sdružování základnového zpracování (jako v C-RAN), kde mohou být zpracovatelské zdroje z mnoho buněk agregovány v centrální ústředně, což vede k lepšímu využití zdrojů, snazší údržbě a efektivnější podpoře funkcí jako koordinované plánování. Také usnadňuje nasazení dálkových rádiových hlav ([RRH](/mobilnisite/slovnik/rrh/)), které jsou menší a mohou být umístěny blíže anténám, čímž se snižují ztráty v napájecích kabelech a zlepšuje se pokrytí a energetická účinnost. Standardizace tohoto rozhraní, naznačená v odkazovaných 3GPP specifikacích, byla motivována snahou odvětví směřovat k otevřeným a disagregovaným RAN architekturám.

Historicky proprietární rozhraní omezovala flexibilitu. Tlak na standardizaci NDI, často v souladu s průmyslovými fóry jako je O-RAN Alliance, si klade za cíl vytvořit více-dodavatelský ekosystém. To snižuje kapitálové i provozní výdaje operátorů a urychluje adopci pokročilých RAN funkcí. Ve verzích jako Rel-16 a novějších se účel rozšiřuje o podporu nových požadavků 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB) s velmi vysokou propustností, ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a přesné časování potřebné pro síťovou synchronizaci napříč rozdělenými architekturami.

## Klíčové vlastnosti

- Standardizuje propojení mezi základnovými a rádiovými jednotkami
- Podporuje vysokorychlostní přenos digitalizovaných rádiových vzorků I/Q
- Definuje protokoly fyzické vrstvy (např. optické) a linkové vrstvy
- Přenáší multiplexovaná uživatelská data, řídicí data a synchronizační data
- Umožňuje komunikaci s nízkou, deterministickou latencí pro rádiové časování
- Usnadňuje více-dodavatelskou interoperabilitu v disagregovaném RAN

## Definující specifikace

- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ndi/)
