---
slug: "p-csi"
url: "/mobilnisite/slovnik/p-csi/"
type: "slovnik"
title: "P-CSI – Periodic Channel State Information"
date: 2025-01-01
abbr: "P-CSI"
fullName: "Periodic Channel State Information"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/p-csi/"
summary: "Periodic Channel State Information (P-CSI, periodické hlášení stavu kanálu) je mechanismus hlášení v 5G NR, kde UE přenáší informace o kvalitě kanálu, předkódování a hodnosti (rank) k gNB v pravidelný"
---

P-CSI je mechanismus hlášení v 5G NR, kde UE (uživatelské zařízení) přenáší informace o stavu kanálu k gNB (základnové stanici) v pravidelných intervalech pro adaptaci spojení a plánování.

## Popis

Periodic Channel State Information (P-CSI, periodické hlášení stavu kanálu) je základní schéma zpětného hlášení v rozhraní 5G New Radio (NR), standardizované 3GPP počínaje Release 15 a vylepšené v pozdějších vydáních. Je jedním z několika typů hlášení [CSI](/mobilnisite/slovnik/csi/) – vedle Aperiodic ([A-CSI](/mobilnisite/slovnik/a-csi/)) a Semi-Persistent (SP-CSI) – které gNodeB (gNB) konfiguruje pro User Equipment (UE), aby sdělovalo podrobné informace o downlink rádiovém kanálu. Hlášení P-CSI jsou přenášena UE autonomně v předdefinovaných periodických intervalech s využitím zdrojů řídicího kanálu v uplinku ([PUCCH](/mobilnisite/slovnik/pucch/)), aniž by vyžadovala dynamický downlink grant ke spuštění každého hlášení. To je ideální pro poskytování pravidelných aktualizací stavu kanálu s nízkou režií za relativně stabilních podmínek kanálu.

Technicky je hlášení P-CSI konfigurováno signalizací Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Konfigurace zahrnuje parametry jako periodicitu hlášení (ve slotech), časový offset a specifický obsah CSI, který má být hlášen. Tento obsah může sestávat z více složek: Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)), který doporučuje schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)); Precoding Matrix Indicator ([PMI](/mobilnisite/slovnik/pmi/)), který navrhuje předkódovací matici pro [MIMO](/mobilnisite/slovnik/mimo/) přenosy; Rank Indicator (RI), udávající preferovaný počet prostorových vrstev; a volitelně CSI-RS Resource Indicator (CRI) pro scénáře s více paprsky. UE tyto metriky odvozuje na základě měření nakonfigurovaných referenčních signálů CSI (CSI-RS) vysílaných gNB. Hlášení je pak naformátováno podle nakonfigurovaného kodebooku a přeneseno na zdroji PUCCH, jehož periodicita je synchronizována s časováním hlášení CSI.

V rámci plánovače gNB poskytují hlášení P-CSI kontinuální proud informací o kanálu, i když pro UE není naplánována žádná downlink data. To umožňuje gNB udržovat aktuální přehled o kvalitě kanálu pro potenciální budoucí přenosy, což umožňuje efektivní adaptaci spojení (výběr správného MCS) a rozhodování o MIMO předkódování. Ve srovnání s A-CSI, které je spouštěno downlink control information (DCI) a poskytuje podrobnější zpětnou vazbu na vyžádání často na PUSCH, má P-CSI nižší signalizační režii a je vždy dostupné, ale může být méně aktuální v rychle se měnícím prostředí. gNB může dynamicky aktivovat, deaktivovat nebo překonfigurovat hlášení P-CSI pomocí Medium Access Control (MAC) Control Elements (CEs) nebo RRC rekonfigurace, což umožňuje flexibilní adaptaci na vzorce provozu a stavy mobility. V pokročilých nasazeních podporuje P-CSI operace s více panely a více TRP (Transmission Reception Point), poskytujíc zpětnou vazbu komplexního CSI pro koherentní společný přenos.

## K čemu slouží

Hlášení P-CSI bylo zavedeno v 5G NR, aby řešilo potřebu efektivní, kontinuální zpětné vazby o kanálu v širokém spektru scénářů nasazení, od enhanced mobile broadband (eMBB) po ultra-reliable low-latency communications (URLLC). V LTE se také používalo periodické hlášení CSI na PUCCH, ale flexibilnější numerologie 5G, širší šířky pásma a pokročilá MIMO schémata vyžadovala sofistikovanější rámec. P-CSI řeší problém udržování povědomí o stavu kanálu bez neustálé režie spouštění, což je klíčové pro plánování provozu citlivého na latenci nebo pro správu spojení se semi-persistent scheduling (SPS).

Historicky systémy bez periodické zpětné vazby spoléhaly pouze na aperiodická hlášení spouštěná plánováním dat, což mohlo vést k zastaralým informacím o kanálu během nečinných období, způsobujíc selhání počátečních přenosů nebo konzervativní výběr MCS. P-CSI zajišťuje, že gNB má vždy aktuální odhad kanálu, což umožňuje rychlejší rozhodování o plánování a vyšší spektrální účinnost. To je obzvláště důležité pro využití massive MIMO a beamformingu v 5G, kde optimální předkódování závisí na přesném a častém CSI.

Návrh P-CSI v Release 15 a jeho vylepšení v Release 16-19 také podporují rostoucí složitost nasazení 5G. Například v operacích s více paprsky může P-CSI hlásit kvality specifické pro paprsek, což napomáhá správě paprsků. Pro úsporu energie sítě lze P-CSI konfigurovat s dlouhou periodicitou během nízké aktivity. Jeho flexibilita umožňuje operátorům vyvážit přesnost zpětné vazby, režii v uplinku a spotřebu energie UE, což z něj činí základní kámen adaptivního řízení rádiových zdrojů v 5G.

## Klíčové vlastnosti

- Přenášeno UE autonomně v nakonfigurovaných periodických intervalech na PUCCH bez spouštění DCI.
- Hlásí klíčové metriky kanálu: CQI, PMI, RI a volitelně CRI pro správu paprsků.
- Konfigurováno pomocí RRC signalizace s parametry pro periodicitu, offset a hlášený obsah.
- Podporuje více nastavení hlášení CSI pro různé části šířky pásma (BWP) a komponentní nosné.
- Lze dynamicky aktivovat/deaktivovat nebo překonfigurovat pomocí MAC CE pro síťovou flexibilitu.
- Poskytuje kontinuální povědomí o stavu kanálu pro plánování gNB a adaptaci spojení, optimalizuje výkon v polostatických podmínkách.

## Související pojmy

- [A-CSI – Aperiodic Channel State Information](/mobilnisite/slovnik/a-csi/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [PMI – Precoding Matrix Indicator](/mobilnisite/slovnik/pmi/)
- [RI – Roaming Intermediary](/mobilnisite/slovnik/ri/)

## Definující specifikace

- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [P-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-csi/)
