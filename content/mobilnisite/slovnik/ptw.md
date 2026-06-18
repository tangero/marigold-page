---
slug: "ptw"
url: "/mobilnisite/slovnik/ptw/"
type: "slovnik"
title: "PTW – Paging Transmission Window"
date: 2025-01-01
abbr: "PTW"
fullName: "Paging Transmission Window"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptw/"
summary: "Definované časové okno v rámci cyklu pagingu, během kterého UE monitoruje pagingové zprávy. Jde o klíčový mechanismus pro úsporu energie UE ve stavech RRC_IDLE a RRC_INACTIVE, který výrazně prodlužuje"
---

PTW je definované časové okno v rámci cyklu pagingu, během kterého UE monitoruje pagingové zprávy za účelem úspory energie ve stavech RRC_IDLE a RRC_INACTIVE.

## Popis

Paging Transmission Window (PTW) je základní koncept v mechanismech pro úsporu energie podle 3GPP, specificky definovaný pro zařízení eMTC (enhanced Machine-Type Communication) a NB-IoT (Narrowband IoT). Funguje v rámci širšího rámce rozšířeného cyklu nespojitého příjmu (eDRX). Základní princip spočívá v soustředění pagingových přenosů sítě pro konkrétní UE do předvídatelného a ohraničeného časového okna, namísto jejich rozptylování po celém potenciálně velmi dlouhém cyklu eDRX. To umožňuje UE vypnout svůj rádiový přijímač po velkou většinu cyklu a probudit se pouze během přiřazeného PTW, aby zkontrolovala příchozí paging.

Z architektonického hlediska je PTW konfigurováno sítí prostřednictvím signalizace Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Mezi parametry patří délka PTW a jeho vztah k cyklu eDRX. UE vypočítá přesné načasování svého PTW na základě svého jedinečného identifikátoru (jako je [IMSI](/mobilnisite/slovnik/imsi/)), systémových informací a nakonfigurovaných parametrů. Během PTW UE monitoruje své přiřazené pagingové příležitosti ([PO](/mobilnisite/slovnik/po/)) podle pravidel standardního pagingového postupu, ale tyto PO jsou nyní omezeny tak, aby spadaly do doby trvání PTW. Síť, která zná rozvrh PTW UE, se pokusí o paging této UE pouze během tohoto okna.

Z procesního hlediska, když dorazí datový paket nebo signalizační zpráva pro UE ve stavu [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE, core network spustí pagingový postup. Access Stratum v RAN naplánuje přenos pagingové zprávy do konkrétního PO. Pro UE používající PTW RAN zajistí, že toto PO je naplánováno během aktivního PTW dané UE. Pokud UE úspěšně přijme pagingovou zprávu adresovanou jí, zahájí proceduru náhodného přístupu pro přechod do stavu RRC_CONNECTED. Pokud do konce PTW není přijat žádný paging, UE se vrátí do stavu hlubokého spánku až do začátku dalšího PTW.

Role PTW je klíčová pro vyvážení dosažitelnosti v síti a spotřeby energie zařízení. Pro aplikace IoT a [MTC](/mobilnisite/slovnik/mtc/), kde zařízení hlásí zřídka a musí fungovat na baterie po celé roky, je schopnost prodloužit doby spánku ze sekund (s normálním [DRX](/mobilnisite/slovnik/drx/)) na minuty, hodiny nebo dokonce dny (s eDRX+PTW) přelomová. Přímo umožňuje dosažení cílů dlouhé výdrže baterie přes 10 let pro mnohé use case massive IoT. PTW poskytuje deterministické 'zapnuté' okno, což zjednodušuje jak implementaci UE, tak síťové plánování ve srovnání s čistě pravděpodobnostními schématy dlouhého spánku.

## K čemu slouží

PTW bylo zavedeno, aby řešilo přísné požadavky na spotřebu energie zařízení massive Machine-Type Communication (mMTC) a Internetu věcí (IoT) definované v 3GPP Release 13 a novějších. Před eDRX a PTW používaly UE standardní cykly nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)), které byly omezeny maximálně na několik sekund. Pro senzory nebo měřiče, které odesílají data pouze několikrát denně, bylo probouzení každých několik sekund za účelem kontroly pagingu obrovským a plýtvavým odběrem z baterie, což činilo buněčnou konektivitu nepraktickou pro dlouhověká zařízení napájená bateriemi.

Primární problém, který PTW řeší, je prodloužení dob spánku při zachování zvládnutelné latence pro služby iniciované sítí (mobile-terminated). Pouhé prodloužení cyklu DRX bez PTW by znamenalo, že pagingové příležitosti UE by byly rozptýleny po velmi dlouhém období. To by nutilo síť opakovaně vysílat pagingové zprávy po mnoha subrámcích, aby zajistila pokrytí, což by plýtvalo rádiovými prostředky a mohlo by zkomplikovat implementaci UE. PTW poskytuje soustředěné období 'aktivního naslouchání', což činí pagingový proces efektivním jak pro síť, tak pro UE.

Historicky vzešla motivace z průmyslových odvětví, jako jsou utility, sledování majetku a chytrá města, která vyžadovala konektivitu na úrovni mobilních sítí, ale s výdrží baterie měřenou v letech, nikoli dnech. PTW v kombinaci s cyklem eDRX se stalo klíčovým řešením 3GPP pro splnění těchto požadavků, což umožnilo LTE-M a NB-IoT konkurovat neceliálním LPWAN technologiím. Představuje zásadní posun od konektivity 'vždy připraven' ke konektivitě 'předvídatelně dosažitelná', optimalizované pro energetickou účinnost na úkor okamžité odezvy.

## Klíčové vlastnosti

- Definuje ohraničené časové okno pro příjem pagingu v rámci dlouhého cyklu eDRX
- Konfigurováno prostřednictvím NAS signalizace (např. timer T3324) pro řízení core networkem
- Umožňuje extrémní úsporu energie UE minimalizací doby zapnutí přijímače
- Funguje v součinnosti s výpočty Paging Occasion (PO) a Paging Frame (PF)
- Aplikovatelné pro stavy RRC_IDLE i RRC_INACTIVE pro eMTC a NB-IoT
- Poskytuje deterministické chování pro síťové plánování pagingových zpráv

## Definující specifikace

- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [PTW na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptw/)
