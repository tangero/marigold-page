---
slug: "pacch"
url: "/mobilnisite/slovnik/pacch/"
type: "slovnik"
title: "PACCH – Packet Associated Control Channel"
date: 2025-01-01
abbr: "PACCH"
fullName: "Packet Associated Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pacch/"
summary: "Logický kanál v sítích GPRS/EDGE, který přenáší signalizační a řídicí informace spojené s paketovým datovým provozem (TBF) konkrétního uživatele. Je nezbytný pro správu přiřazení zdrojů v uplinku a do"
---

PACCH je logický kanál v sítích GPRS/EDGE, který přenáší signalizační a řídicí informace pro paketový datový provoz konkrétního uživatele za účelem správy přiřazení zdrojů, řízení výkonu a potvrzení.

## Popis

Packet Associated Control Channel (PACCH) je základní logický řídicí kanál v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) určený pro paketově přepínané služby zavedené s [GPRS](/mobilnisite/slovnik/gprs/). Funguje ve spojení s Temporary Block Flow ([TBF](/mobilnisite/slovnik/tbf/)), což je fyzické spojení zřízené pro přenos paketových datových jednotek. Na rozdíl od společných řídicích kanálů je PACCH jednoznačně spojen s konkrétním TBF uživatele. Jeho hlavní funkcí je přenos signalizace v pásmu nezbytné pro správu tohoto TBF v reálném čase. To zahrnuje klíčové zprávy pro přiřazení zdrojů, například alokaci paketových datových kanálů ([PDCH](/mobilnisite/slovnik/pdch/)) pro uplink a downlink, a pro adaptaci spojení, jako jsou příkazy pro řízení výkonu a úpravy časového předstihu pro udržení kvality rádiového spojení.

Architektonicky PACCH sdílí stejné fyzické rádiové prostředky (časové sloty) jako Packet Data Traffic Channel ([PDTCH](/mobilnisite/slovnik/pdtch/)) přiřazený uživateli. Nemá vyhrazené časové sloty; místo toho dynamicky obsazuje bloky uvnitř přiřazených PDCH. Toto multiplexování řídí vrstva Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Když je mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) zapojena do paketového přenosu, síť může posílat řídicí zprávy na downlink PACCH k MS a MS může posílat řídicí zprávy na uplink PACCH do sítě. Mezi klíčové typy zpráv patří například zprávy Packet Uplink/Downlink Assignment, které přidělují rádiové bloky pro datový přenos, a zprávy Packet Control Acknowledgment, které poskytují potvrzení o přijetí RLC/MAC bloků.

Úloha PACCH je klíčová pro efektivní správu rádiových zdrojů. Umožňuje síti dynamicky reagovat na měnící se podmínky kanálu a požadavky na data bez zrušení TBF. Například pokud se kvalita kanálu zhorší, může síť použít PACCH k nařízení snížení kódovacího schématu nebo zvýšení vysílacího výkonu. PACCH také přenáší pollingové požadavky a odpovědi, které se používají pro hlášení stavu a řešení kolizí. Přidružení kanálu ke konkrétnímu TBF zajišťuje včasnou a cílenou signalizaci, což minimalizuje latenci řídicích příkazů ve srovnání s použitím společných kanálů, které by vyžadovaly adresování a řešení kolizí. Tento koncept je základním kamenem paketově orientované evoluce GSM a poskytuje nezbytnou agilitu pro přerušovaný (bursty) datový provoz.

## K čemu slouží

PACCH byl vytvořen, aby odstranil základní omezení klasických sítí GSM, které byly navrženy primárně pro okruhově přepínanou hlasovou komunikaci. V okruhově přepínaném režimu byly vyhrazené signalizační kanály (jako SACCH) po dobu trvání hovoru trvale spojeny s kanálem pro přenos hovoru. Pro paketová data jsou však zdroje přidělovány na vyžádání v krátkých impulsech. Trvalý, vyhrazený signalizační kanál pro každého potenciálního datového uživatele by byl extrémně nehospodárný vůči vzácnému rádiovému spektru.

Zavedení GPRS vyžadovalo nový, efektivní mechanismus pro doručování řídicí signalizace specificky vázané na pomíjivou, impulzově orientovanou povahu paketových datových přenosů. PACCH tento problém řeší tím, že je dynamicky přidružen pouze k aktivnímu Temporary Block Flow (TBF). Znovu využívá stejné fyzické prostředky jako datový přenos, čímž odstraňuje potřebu samostatného, trvale přiděleného signalizačního kanálu. Tento návrh optimalizuje spektrální účinnost, což byl klíčový požadavek pro rané mobilní datové služby. Umožňuje síti provádět nezbytné funkce, jako je pře-přiřazení zdrojů, adaptace spojení a potvrzování, s minimální režií a latencí, a tím přímo podporovat kvalitu služeb pro paketové datové aplikace.

Historicky by bez kanálu, jako je PACCH, správa paketové datové relace vyžadovala neustálé nastavování a rušení signalizačních kontextů pomocí společných řídicích kanálů, což by přinášelo významné zpoždění a signalizační zátěž. PACCH poskytl nezbytnou řídicí rovinu v rámci relace, což umožnilo GPRS nabízet důvěryhodnou a efektivní datovou službu nad stávající infrastrukturou GSM. Byl klíčovým prvkem pro prostředí neustálého datového připojení (always-on), protože umožňoval prokládání řídicích zpráv s datovými bloky bez přerušení toku dat.

## Klíčové vlastnosti

- Dynamicky přidružen ke konkrétnímu Temporary Block Flow (TBF)
- Sdílí fyzické prostředky (PDCH) s přidruženým PDTCH
- Přenáší klíčovou signalizaci pro správu TBF (přiřazení, potvrzení)
- Podporuje přenos řídicích zpráv v uplinku i downlinku
- Umožňuje adaptaci spojení v reálném čase (řízení výkonu, časový předstih)
- Používá se pro polling a hlášení stavu během aktivního datového přenosu

## Související pojmy

- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [PDTCH – Packet Data Traffic Channel](/mobilnisite/slovnik/pdtch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TR 44.901** (Rel-19) — Extended NACC for External Cell Change

---

📖 **Anglický originál a plná specifikace:** [PACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pacch/)
