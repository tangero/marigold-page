---
slug: "cdrx"
url: "/mobilnisite/slovnik/cdrx/"
type: "slovnik"
title: "CDRX – Connected mode Discontinuous Reception"
date: 2025-01-01
abbr: "CDRX"
fullName: "Connected mode Discontinuous Reception"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdrx/"
summary: "CDRX je mechanismus pro úsporu energie u koncového zařízení (UE) v připojeném režimu, který mu umožňuje pravidelně vypínat svůj přijímač během nečinnosti při zachování RRC spojení. Významně prodlužuje"
---

CDRX je mechanismus pro úsporu energie u koncového zařízení v připojeném režimu, který mu umožňuje pravidelně vypínat svůj přijímač během nečinnosti při zachování RRC spojení, čímž prodlužuje výdrž baterie.

## Popis

Connected mode Discontinuous Reception (CDRX) je sofistikovaná technika pro úsporu energie definovaná ve specifikacích 3GPP, primárně pro sítě 5G NR (New Radio) a LTE. Funguje tak, že umožňuje UE přejít do stavu s nízkou spotřebou během předdefinovaných period nečinnosti, zatímco zůstává ve stavu [RRC](/mobilnisite/slovnik/rrc/)_CONNECTED, čímž se vyhne signalizační režii a latenci spojené s přechodem do režimu idle. Síť konfiguruje parametry CDRX prostřednictvím RRC signalizace, včetně časovače On Duration, časovače Inactivity a délky [DRX](/mobilnisite/slovnik/drx/) cyklu, které určují vzory spánku a probouzení UE. Během On Duration monitoruje UE fyzický downlinkový řídicí kanál ([PDCCH](/mobilnisite/slovnik/pdcch/)) pro potenciální naplánování přenosů; pokud není detekována žádná aktivita, přejde do spánkového stavu až do dalšího cyklu, čímž šetří energii baterie bez přerušení spojení.

Z architektonického hlediska CDRX zahrnuje koordinaci mezi UE a gNB (v 5G) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE), přičemž síť dynamicky upravuje parametry na základě charakteristik provozu, požadavků QoS a schopností UE. Mezi klíčové komponenty patří časovače jako drx-onDurationTimer, drx-InactivityTimer a drx-RetransmissionTimer, které spravují přijímací okna UE pro počáteční přenosy, následné plánování a [HARQ](/mobilnisite/slovnik/harq/) retransmise. Mechanismus podporuje jak dlouhé, tak krátké DRX cykly, což umožňuje flexibilitu pro různé potřeby aplikací – např. krátké cykly pro služby citlivé na latenci a dlouhé cykly pro přenosy na pozadí. Tato podrobná kontrola zajišťuje maximalizaci úspor energie bez kompromisů v uživatelském komfortu nebo odezvě sítě.

Během provozu CDRX využívá schopnost UE rychle přepínat mezi aktivním a spícím stavem, přičemž síť během spánkových period buffruje data a plánuje přenosy během aktivních intervalů. UE naslouchá downlinkovým řídicím informacím ([DCI](/mobilnisite/slovnik/dci/)) na PDCCH během svých aktivních oken; pokud je naplánována, zůstane vzhůru pro příjem dat a podle toho resetuje časovače. Pro uplinkový provoz může UE odesílat Scheduling Requests (SR) nebo používat configured grants, aby sladila přenosy se svými aktivními fázemi. Tato synchronizace minimalizuje zbytečnou rádiovou aktivitu, snižuje interference a zlepšuje celkovou kapacitu sítě. CDRX je nedílnou součástí cílů 5G v oblasti energetické účinnosti a podporuje rozmanité use case od rozšířeného mobilního širokopásmového připojení po hromadná IoT nasazení.

Role CDRX přesahuje rámec úspor energie a ovlivňuje výkon sítě a mobilitu UE. Udržováním RRC spojení umožňuje rychlejší přechody mezi stavy a sníženou latenci pro sporadické datové přenosy, což je zásadní pro aplikace jako instant messaging nebo push notifikace. V mobilních scénářích lze parametry CDRX přizpůsobit během handoverů, aby byl zajištěn plynulý provoz. Mechanismus také interaguje s dalšími funkcemi, jako je adaptace [BWP](/mobilnisite/slovnik/bwp/) (Bandwidth Part) a SPS (Semi-Persistent Scheduling), což umožňuje další optimalizaci. Pro IoT zařízení je CDRX často kombinováno s eDRX (extended DRX) pro prodloužené spánkové cykly, což vyvažuje výdrž baterie s požadavky na dosažitelnost. Celkově CDRX představuje klíčový prvek pro udržitelné a efektivní bezdrátové sítě.

## K čemu slouží

CDRX bylo zavedeno, aby řešilo rostoucí poptávku po delší výdrži baterie mobilních zařízení, zejména proto, že 5G sítě podporují vyšší datové rychlosti a častější připojení, což tradičně zvyšuje spotřebu energie. Před zavedením CDRX musela UE v připojeném režimu nepřetržitě monitorovat řídicí kanály, což vedlo k významnému odběru energie během období nízké aktivity. To bylo neudržitelné pro neustále připojené aplikace a IoT nasazení, kde zařízení musí zůstat připojena po dlouhou dobu bez častého dobíjení. CDRX to řeší tím, že umožňuje UE šetřit energii během nečinnosti, a zároveň se vyhne latenci a signalizační režii spojené s přechodem do [RRC](/mobilnisite/slovnik/rrc/)_IDLE, čímž udržuje rovnováhu mezi odezvou a efektivitou.

Vznik CDRX byl motivován rozšířením chytrých telefonů, nositelných zařízení a IoT senzorů, které vyžadují trvalé síťové připojení pro služby jako jsou notifikace v reálném čase, cloudová synchronizace a komunikace s nízkou latencí. V LTE existovaly základní DRX mechanismy, ale v 5G byly vylepšeny, aby zvládly dynamičtější charakteristiky provozu a rozmanité QoS profily. CDRX poskytuje jemnější kontrolu nad spánkovými cykly, přizpůsobuje se chování aplikace – např. snižuje spotřebu pro aktualizace na pozadí, ale zajišťuje rychlé probuzení pro interaktivní relace. Tím řeší omezení dřívějších přístupů, které buď udržovaly UE plně aktivní, nebo vynucovaly časté změny stavu, což ohrožovalo buď výdrž baterie, nebo uživatelský komfort.

Historicky nabízely techniky úspory energie jako PSM (Power Saving Mode) hluboký spánek, ale s vysokou latencí, zatímco nepřetržitý příjem byl energeticky náročný. CDRX tuto mezeru zaplňuje tím, že umožňuje diskontinuální příjem uvnitř připojeného stavu, což je koncept zdokonalovaný v rámci vydání 3GPP pro podporu nových use case. Zarovnává se s cíli 5G v oblasti energeticky účinných sítí a udržitelného provozu, snižuje uhlíkovou stopu zařízení a infrastruktury. Řešením kritického problému vybíjení baterie v připojeném režimu CDRX usnadňuje adopci 5G pro neustále připojená zařízení, od spotřební elektroniky po průmyslové IoT, a zajišťuje, že pokroky v rychlosti a kapacitě neprobíhají na úkor použitelnosti.

## Klíčové vlastnosti

- Konfigurovatelné DRX cykly (dlouhé a krátké) pro adaptivní správu spotřeby
- Dynamický provoz založený na časovačích včetně časovačů On Duration, Inactivity a Retransmission
- Podpora HARQ retransmisí během aktivních oken pro zachování spolehlivosti
- Integrace s adaptací BWP a SPS pro další úspory energie
- Kompatibilita s mobilními procedurami, jako jsou handovery, bez narušení spánkových vzorů
- Vylepšení pro IoT prostřednictvím kombinace s eDRX a wake-up signalizací

## Související pojmy

- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [BWP – Bandwidth Part](/mobilnisite/slovnik/bwp/)

## Definující specifikace

- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TR 26.910** (Rel-19) — MTSI enhancements for RAN delay budget reporting
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR

---

📖 **Anglický originál a plná specifikace:** [CDRX na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdrx/)
