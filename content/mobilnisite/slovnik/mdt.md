---
slug: "mdt"
url: "/mobilnisite/slovnik/mdt/"
type: "slovnik"
title: "MDT – Minimization of Drive Tests"
date: 2026-01-01
abbr: "MDT"
fullName: "Minimization of Drive Tests"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mdt/"
summary: "Funkce 3GPP, která automatizuje monitorování výkonu sítě sběrem měření z uživatelských zařízení (UE) a základnových stanic. Snižuje potřebu nákladných a časově náročných manuálních drive testů a umožň"
---

MDT je funkce 3GPP, která automatizuje monitorování výkonu sítě sběrem měření z uživatelských zařízení a základnových stanic za účelem snížení potřeby manuálních drive testů.

## Popis

Minimization of Drive Tests (MDT) je funkce správy a optimalizace sítě standardizovaná napříč releasy 3GPP. Jejím hlavním účelem je automatizovaný sběr rádiových měření, informací o poloze a dalších relevantních dat od účastnících se uživatelských zařízení (UE) a stanic eNodeB ([eNB](/mobilnisite/slovnik/enb/)/gNB) řízeným způsobem. Tato data jsou následně hlášena systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo entitě pro sběr trasování k analýze. MDT mění pasivní uživatelská zařízení na aktivní sondy sítě a poskytuje detailní pohled na výkon sítě, pokrytí a kvalitu služeb (QoS) z perspektivy koncového uživatele v reálném provozu.

Z architektonického hlediska se MDT účastní několik klíčových síťových prvků. Systém řízení (např. OAM) konfiguruje úlohy MDT, specifikuje, jaká měření se mají sbírat (např. Reference Signal Received Power (RSRP), Reference Signal Received Quality (RSRQ), propustnost), za jakých podmínek (okamžitě nebo s logováním) a od kterých uživatelských zařízení (na základě oblasti, předplatného atd.). Tato konfigurace je komunikována do rádiové přístupové sítě (RAN) přes rozhraní Itf-N (mezi OAM a RAN) nebo uvnitř RAN. Uzel RAN (eNB/gNB) následně aktivuje MDT pro vybraná uživatelská zařízení pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/). Uživatelská zařízení provedou požadovaná měření, která mohou být nahlášena okamžitě (Immediate MDT) nebo uložena lokálně a nahlášena později při opětovném připojení (Logged MDT). Informace o poloze mohou být získány pomocí [GNSS](/mobilnisite/slovnik/gnss/) v uživatelském zařízení, pozicování založeném na síti nebo RF fingerprintingu. Sběrané reporty MDT jsou nakonec agregovány v systému správy sítě ke zpracování a analýze.

MDT funguje ve dvou hlavních módech: Immediate MDT a Logged MDT. Immediate MDT provádějí uživatelská zařízení ve stavu RRC_CONNECTED a měření jsou hlášena přímo síti. Tento mód je užitečný pro řešení problémů v reálném čase. Logged MDT provádějí uživatelská zařízení ve stavech RRC_IDLE nebo RRC_INACTIVE; měření jsou uložena v interním logu s časovými značkami a informacemi o poloze (pokud jsou dostupné) a jsou nahlášena, když se uživatelské zařízení přepne zpět do stavu RRC_CONNECTED. Tento mód je neocenitelný pro optimalizaci pokrytí, zejména v oblastech se špatným signálem. Sběraná data poskytují přehled o dírách v pokrytí, pilotní interferenci, selháních předávání hovorů a degradaci QoS, což umožňuje plánování a optimalizaci sítě založené na datech.

## K čemu slouží

MDT bylo vytvořeno, aby řešilo významné provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a omezení spojená s tradičními manuálními drive testy. Manuální testy jsou nákladné, časově náročné, poskytují pouze momentální snímek stavu, nemohou pokrýt všechny geografické oblasti (např. vnitřní prostory, soukromé pozemky) a postrádají kontext koncového uživatele pro datové služby. Jak sítě s příchodem 3G a 4G houstly a stávaly se složitějšími, tato omezení se pro operátory usilující o udržení vysoké kvality služeb stávala stále větší zátěží.

Tato technologie řeší problém neefektivního a neúplného monitorování výkonu sítě využitím existující flotily uživatelských zařízení jako distribuovaných senzorů. To poskytuje kontinuální, rozsáhlá a na uživatele zaměřená data, která odrážejí skutečný uživatelský zážitek ze služeb. Umožňuje proaktivní optimalizaci sítě, rychlejší detekci chyb a přesnější plánování kapacity. Historicky bylo MDT zavedeno ve 3GPP Release 9 pro LTE a později rozšířeno na UMTS, GSM a NR, čímž se stalo základním kamenem funkcionalit samoorganizujících se sítí (SON).

MDT vyřešilo klíčové omezení předchozích přístupů – nedostatek škálovatelného a všudypřítomného sběru měření – standardizací procedur pro sběr a reportování měření z uživatelských zařízení. To umožnilo operátorům přejít od reaktivní optimalizace založené na vzorcích k paradigmatu optimalizace založené na datech a probíhající kontinuálně. Motivací byl tlak průmyslu směrem k automatizaci (SON) a potřeba nákladově efektivně spravovat stále heterogennější a hustší sítě.

## Klíčové vlastnosti

- Automatizovaný sběr měření z uživatelských zařízení a buněk (RSRP, RSRQ atd.)
- Podpora dvou módů: Immediate MDT (stav připojení) a Logged MDT (stav nečinnosti/neaktivity)
- Zahrnuje informace o poloze uživatelského zařízení (GNSS, RF fingerprinting)
- Konfigurovatelné systémem řízení (OAM) pro cílený sběr dat
- Umožňuje monitorování výkonu sítě a kvality uživatelského prožitku (QoE) zaměřené na uživatele
- Základ pro pokročilé případy užití samoorganizujících se sítí (SON), jako je optimalizace pokrytí a kapacity

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 26.909** (Rel-19) — QoE Enhancement for Streaming Services
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TR 28.837** (Rel-18) — Technical Report on Trace/MDT Management
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [MDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdt/)
