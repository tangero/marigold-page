---
slug: "lbs"
url: "/mobilnisite/slovnik/lbs/"
type: "slovnik"
title: "LBS – Location Based Services"
date: 2025-01-01
abbr: "LBS"
fullName: "Location Based Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lbs/"
summary: "Soubor služeb a síťových schopností, které využívají geografickou polohu uživatelského zařízení (UE) k poskytování služeb s přidanou hodnotou. Patří mezi ně tísňové služby (např. E911), navigace, rekl"
---

LBS je soubor služeb a síťových schopností, které využívají geografickou polohu mobilního zařízení k poskytování služeb s přidanou hodnotou, jako jsou tísňové služby, navigace a reklama založená na poloze.

## Popis

Služby založené na poloze (LBS) v rámci 3GPP zahrnují standardizované architektury, protokoly a funkce, které umožňují síťovým operátorům a poskytovatelům služeb třetích stran zjistit zeměpisnou polohu mobilního zařízení a poskytovat služby na základě této informace. Architektura je postavena kolem klíčových síťových funkcí: funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v 5GC, brány centra polohy mobilních zařízení ([GMLC](/mobilnisite/slovnik/gmlc/)), která slouží jako brána pro externí požadavky na polohu, a samotného UE, které může mít integrované schopnosti globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)). Centrum polohy mobilních zařízení ([SMLC](/mobilnisite/slovnik/smlc/)) nebo jeho evolvovaná verze ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v RAN poskytuje řízení pro síťové metody určování polohy.

Proces funguje na principu požadavek-odpověď. Externí klient služeb založených na poloze ([LCS](/mobilnisite/slovnik/lcs/) Client) nebo interní síťová služba (jako IMS tísňové služby) odešle požadavek na polohu do GMLC. GMLC ověří klienta a přepošle požadavek příslušné síťové entitě jádra ([MME](/mobilnisite/slovnik/mme/) v 4G, [AMF](/mobilnisite/slovnik/amf/) v 5G), která koordinuje spolupráci s uzlem pro určování polohy (E-SMLC/LMF) a s RAN. Samotné určení polohy lze dosáhnout pomocí více metod: síťových metod, jako je OTDOA v LTE/NR nebo UTDOA; metod založených na UE využívajících asistovaný GNSS (A-GNSS), kdy síť poskytuje podpůrná data; nebo hybridních metod. Vypočtený odhad polohy (zeměpisná šířka, délka, nadmořská výška, přesnost) je následně směrován zpět přes řetězec entit k žádajícímu klientovi.

LBS hrají v síti mnohostrannou roli. Jejich nejkritičtější úlohou jsou regulované tísňové služby (např. E112 v EU, E911 v USA), kde přesné a rychlé určení polohy volajícího je otázkou veřejné bezpečnosti. Komerčně umožňují rozsáhlý ekosystém aplikací od navigací po jednotlivých krocích a sociálních sítí až po sledování majetku a doručování obsahu zohledňujícího polohu. Pro síťové operátory jsou data LBS cenná pro plánování sítě, optimalizaci a analytiku. Standardy 3GPP zajišťují interoperabilitu, ochranu soukromí (prostřednictvím mechanismů souhlasu účastníka), zabezpečení a požadavky na výkonnost těchto služeb napříč různými generacemi mobilních sítí.

## K čemu slouží

Hlavním impulzem pro standardizaci LBS byly regulační požadavky na určení polohy tísňových volání, které se v mnoha regionech staly povinnou funkcí po zavedení nařízení, jako je E911 FCC ve Spojených státech. To vytvořilo naléhavou potřebu, aby celulární sítě poskytovaly přesné a spolehlivé informace o poloze bez ohledu na model telefonu nebo uživatelské prostředí, což není schopnost vlastní základnímu buněčnému připojení.

Mimo tísňové služby komerční potenciál znalosti polohy uživatele podnítil vznik široké škály služeb. Raná proprietární řešení byla roztříštěná a neefektivní. Standardizace 3GPP, která naplno začala ve verzi 99, si kladla za cíl vytvořit jednotný, bezpečný a škálovatelný rámec. Vyřešila problémy interoperability mezi síťovými zařízeními a koncovými zařízeními od různých dodavatelů, definovala prvky ochrany soukromí pro ochranu polohových dat účastníka a stanovila výkonnostní měřítka pro přesnost a dobu odezvy. To umožnilo rozvoj globálního trhu pro LBS aplikace, od základních služeb typu "najdi nejbližší" až po komplexní systémy logistiky a správy vozových parků, tím, že poskytlo spolehlivou, na síti nezávislou metodu získání informace o poloze.

## Klíčové vlastnosti

- Podpora více metod určování polohy: A-GNSS, OTDOA, UTDOA, E-CID a metod založených na senzorech
- Standardizovaná kontrola ochrany soukromí a souhlasu (kategorie LCS klientů, upozornění účastníka)
- Architektura podporující procedury určování polohy jak v řídicí rovině, tak v uživatelské rovině
- Spolupráce se satelitními polohovými systémy (GPS, Galileo, GLONASS, BeiDou)
- Podpora určení polohy pro tísňové služby (např. E911, E112) jako regulační požadavek
- Služby polohy pro architektury určování polohy založené na UE i na síti

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication

---

📖 **Anglický originál a plná specifikace:** [LBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lbs/)
