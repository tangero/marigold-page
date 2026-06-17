---
slug: "dtm"
url: "/mobilnisite/slovnik/dtm/"
type: "slovnik"
title: "DTM – Discontinuous Transmission Mode"
date: 2025-01-01
abbr: "DTM"
fullName: "Discontinuous Transmission Mode"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtm/"
summary: "Mechanismus úspory energie v sítích GSM a UMTS, při kterém je vysílač mobilního zařízení vypínán v obdobích bez hlasové aktivity. Snižuje interferenci, šetří životnost baterie UE a zvyšuje celkovou ka"
---

DTM je mechanismus úspory energie v sítích GSM a UMTS, který vypíná vysílač mobilního zařízení během pauz v řeči, aby snížil interferenci, ušetřil baterii a zvýšil kapacitu sítě.

## Popis

Discontinuous Transmission Mode (DTM) je funkce správy rádiových zdrojů používaná v okruhově spínaných hlasových službách GSM (2G) a UMTS (3G). Jejím hlavním účelem je dočasně deaktivovat vysílač rádiových frekvencí mobilní stanice ([MS](/mobilnisite/slovnik/ms/)/UE) během tichých period v hovoru. Lidská řeč má typicky aktivační faktor kolem 40–50 %, což znamená, že vysílač je potřeba pouze přibližně polovinu času během hovoru. DTM toho využívá vypínáním vysílače během tichých intervalů, čímž vznikají takzvané rámce nespojitého vysílání ([DTX](/mobilnisite/slovnik/dtx/)).

Z architektonického hlediska zahrnuje DTM koordinaci mezi UE a podsystémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) v GSM nebo řadičem rádiové sítě (RNC) v UMTS. Síť využívá na úrovni řečového kodeku detektor hlasové aktivity (VAD). Když VAD identifikuje tichou periodu, signalizuje rádiové vrstvě, aby přestala vysílat normální řečové rámce. Místo toho může UE vysílat nízkorychlostní rámce popisovače ticha (SID) v pravidelných intervalech. Tyto SID rámce obsahují parametry pro generování komfortního šumu na přijímací straně, což zabraňuje nepřirozenému přerušování hovoru. Rádiový vysílač je mezi těmito nezbytnými přenosy vypnutý.

Jak to funguje operativně: Během aktivního hovoru fyzická vrstva UE monitoruje výstup řečového kodeku (např. Full Rate, [AMR](/mobilnisite/slovnik/amr/)). Při přechodu z řeči do ticha protokolový zásobník nařídí vysílači ukončit nepřetržitý provoz. Načasování je striktně řízeno strukturou TDMA rámců v GSM nebo vyhrazeným kanálem v UMTS. Síť přiřadí UE konkrétní vzor, kdy musí naslouchat (kvůli pagingu nebo řízení) a kdy může vysílat tyto SID aktualizace. Tento vzor je součástí celkového cyklu nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)), ale je specificky přizpůsoben pro aktivní spojení. Tento proces významně snižuje průměrný výstupní výkon výkonového zesilovače UE, což je nejnáročnější součástka na baterii, a tím prodlužuje dobu hovoru. Zároveň snižuje celkovou uplink interferenci v buňce, což umožňuje vyšší kapacitu a lepší kvalitu signálu pro ostatní uživatele.

## K čemu slouží

DTM byl vytvořen, aby řešil dvě základní omezení v raných mobilních sítích: omezenou životnost baterie UE a konečnou kapacitu rádiového spektra. V původním návrhu GSM by vysílač zůstal aktivní na plný výkon po celou dobu hovoru, dokonce i během ticha, což plýtvalo baterií a vytvářelo konstantní uplink interferenci pro ostatní buňky používající stejnou frekvenci. Tato interference omezovala, jak blízko se mohly frekvence znovu použít, a tím omezovala kapacitu sítě.

Zavedení DTM ve fázi GSM Phase 1 (a později vylepšené) poskytlo přímé řešení. Vypínáním vysílače během ticha přímo šetřilo energii baterie, což byl klíčový prodejní argument pro mobilní telefony. Z pohledu sítě snížení průměrné uplink interference téměř o 50 % umožnilo plánovačům sítí implementovat těsnější vzory opakovaného využití frekvencí, což dramaticky zvýšilo počet hovorů, které dané množství spektra mohlo podporovat. Toto byla klíčová inovace, která učinila z GSM vysokokapacitní, komerčně životaschopný systém. V UMTS (WCDMA) zůstal účel podobný, ačkoli v systému [CDMA](/mobilnisite/slovnik/cdma/) snížení interference přímo znamená zvýšení kapacity kvůli tomu, že kapacita buňky je limitována interferencí. DTM se tedy vyvinul z jednoduché funkce pro úsporu energie v kritickou technologii zvyšující kapacitu pro hlasové sítě 2G a 3G.

## Klíčové vlastnosti

- Dynamicky vypíná vysílač UE během period ticha v řeči
- Používá detekci hlasové aktivity (VAD) k aktivaci změn stavu vysílání
- Vysílá periodické rámce popisovače ticha (SID) pro umožnění generování komfortního šumu
- Snižuje uplink ko-kanálovou interferenci, čímž zvyšuje celkovou kapacitu sítě
- Významně prodlužuje životnost baterie UE během hlasových hovorů
- Integrováno s činností řečového kodeku (např. FR, HR, EFR, AMR)

## Související pojmy

- [DTX – Discontinuous Transmission](/mobilnisite/slovnik/dtx/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 43.055** (Rel-19) — Dual Transfer Mode (DTM) for GSM/GPRS
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [DTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtm/)
