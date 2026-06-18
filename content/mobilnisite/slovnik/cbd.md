---
slug: "cbd"
url: "/mobilnisite/slovnik/cbd/"
type: "slovnik"
title: "CBD – Candidate Beam Detection"
date: 2025-01-01
abbr: "CBD"
fullName: "Candidate Beam Detection"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbd/"
summary: "Candidate Beam Detection (CBD) je procedura správy paprsků v 5G NR, která umožňuje UE identifikovat a hlásit potenciální kandidátní paprsky gNB. Je klíčová pro udržení robustní konektivity, zejména v"
---

CBD je procedura správy paprsků v 5G NR, při které UE identifikuje a hlásí potenciální kandidátní paprsky gNB pro rychlé obnovení a robustní konektivitu, zejména v nasazeních mmWave s úzkými paprsky.

## Popis

Candidate Beam Detection (CBD) je základní mechanismus správy paprsků definovaný v rámci 5G New Radio (NR), určený speciálně pro provoz ve frekvenčním rozsahu 2 (FR2), který zahrnuje pásma milimetrových vln (mmWave). Jeho primární funkcí je proaktivní identifikace alternativních, kvalitních párů paprsků, které mohou sloužit jako záložní, pokud aktuálně aktivní služební paprsek selže nebo se jeho kvalita výrazně zhorší. Tuto proceduru provádí uživatelské zařízení (UE) pod konfigurací a kontrolou gNodeB (gNB). gNB nakonfiguruje UE sadou zdrojů (např. specifických bloků synchronizačních signálů (SSB) nebo referenčních signálů pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/))) odpovídajících kandidátním paprskům. UE poté kontinuálně nebo periodicky měří kvalitu signálu (např. přijatý výkon referenčního signálu ([RSRP](/mobilnisite/slovnik/rsrp/))) těchto nakonfigurovaných kandidátních paprsků, zatímco udržuje svůj primární spojení na služebním paprsku.

Architektonická implementace CBD je integrována do širších procedur vrstvy 1 (fyzické vrstvy) a vrstvy 2 ([MAC](/mobilnisite/slovnik/mac/) vrstvy). gNB odesílá konfigurační parametry prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), která specifikuje zdroje pro měření kandidátních paprsků, kritéria hlášení (prahové hodnoty) a formáty hlášení. Fyzická vrstva UE provádí měření a při splnění předdefinovaných podmínek – například když RSRP kandidátního paprsku překročí RSRP služebního paprsku o určitý offset nebo když kvalita služebního paprsku klesne pod absolutní práh – UE spustí hlášení měření. Toto hlášení je odesláno prostřednictvím řídicích informací v uplinku (např. na [PUCCH](/mobilnisite/slovnik/pucch/) nebo [PUSCH](/mobilnisite/slovnik/pusch/)) a obsahuje identifikátory (např. SSB Resource Indicator (SSBRI) nebo CSI-RS Resource Indicator ([CRI](/mobilnisite/slovnik/cri/))) a naměřenou kvalitu kandidátních paprsků.

Role CBD v síti je klíčová pro mobilitu a robustnost. Poskytuje zásadní informace algoritmům správy paprsků gNB, umožňující rozhodnutí pro zpřesnění paprsku, přepnutí paprsku (uvnitř buňky) nebo předání paprsku mezi buňkami. Díky udržování aktuálního seznamu životaschopných alternativních paprsků může síť provádět procedury obnovy paprsku s minimální latencí, často bez nutnosti návratu k pomalejším procesům detekce a znovunavázání selhání rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)) na úrovni buňky. To je obzvláště důležité pro podporu služeb ultra-spolehlivé komunikace s nízkou latencí (URLLC) a pro udržení konzistentní propustnosti v dynamických mmWave prostředích, kde překážky mohou náhle zastínit dráhu úzkého paprsku.

Klíčové komponenty zapojené do procedury CBD zahrnují konfigurované referenční signály (SSB pro počáteční přístup a režim idle/inactive, CSI-RS pro connected mode), mechanismy měření a filtrování v přijímači UE, spouštěče a kritéria hlášení a algoritmy gNB pro interpretaci hlášení a zahájení příkazů správy paprsků. Procedura funguje ve spojení s dalšími funkcemi správy paprsků, jako je měření paprsků, určení paprsku (na straně gNB) a hlášení o paprsku, čímž vytváří uzavřený regulační systém pro udržování optimálního vyrovnání paprsků.

## K čemu slouží

Candidate Beam Detection byl vytvořen, aby řešil základní výzvy spojené s využitím vysokofrekvenčního mmWave spektra v 5G NR. Zatímco mmWave pásma nabízejí obrovskou šířku pásma pro vícegigabitové datové rychlosti, trpí závažnými charakteristikami šíření, včetně vysokého útlumu na dráze a citlivosti na zastínění (např. budovami, vozidly nebo i uživatelovou rukou). Pro překonání těchto ztrát 5G využívá beamforming s vysoce směrovými anténami, čímž vytváří úzké tužkové paprsky. Toto řešení však vytváří nový problém: spojení na úzkém paprsku je křehké a může být okamžitě přerušeno pohybující se překážkou.

Předchozí mobilní systémy (3G, 4G) pracující na nižších frekvencích používaly širší paprsky na úrovni sektoru. Řízení mobility a předávání (handover) byly primárně založeny na měřeních na úrovni buňky. Náhlé selhání jednotlivého paprsku nebylo běžným režimem selhání. V raných návrzích 5G bylo shledáno nedostatečným spoléhat se při mmWave výhradně na detekci selhání rádiového spoje (RLF) a opětovné připojení. Proces RLF zahrnuje detekci selhání, přerušení spojení, hledání nové buňky a provedení náhodného přístupu – sekvence, která zavádí významnou latenci (stovky milisekund) a přerušení služby, což je nepřijatelné pro klíčové (mission-critical) a vysokopropustné aplikace.

Účelem CBD je proto umožnit proaktivní a rychlou mobilitu na úrovni paprsků. Řeší problém křehkosti paprsku tím, že umožňuje UE a síti mít neustále přehled o alternativních drahách paprsků ještě před selháním toho primárního. To posouvá paradigma od reaktivního obnovení po selhání k proaktivní údržbě spojení. Motivací bylo zajistit, aby teoretické výhody mmWave – vysoká rychlost a kapacita – mohly být realizovány v praktických mobilních scénářích nasazení s nezbytnou spolehlivostí a kvalitou služeb. CBD je klíčovým prvkem umožňujícím naplnění vize 5G o bezproblémové konektivitě ve vysokofrekvenčních pásmech.

## Klíčové vlastnosti

- Proaktivní identifikace záložních párů paprsků před selháním aktivního paprsku
- Měření kandidátních paprsků založené na konfiguraci zdrojů SSB nebo CSI-RS
- Hlášení spouštěné událostmi na základě kvality služebního paprsku a prahových hodnot offsetu kandidátních paprsků
- Umožňuje rychlé přepínání a obnovení paprsku, minimalizuje latenci přerušení služby
- Integrální část frameworku správy paprsků pro provoz mmWave (FR2)
- Podporuje jak zpřesnění paprsku uvnitř buňky, tak přípravu na předání (handover) na úrovni paprsku mezi buňkami

## Definující specifikace

- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification

---

📖 **Anglický originál a plná specifikace:** [CBD na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbd/)
