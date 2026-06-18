---
slug: "cp-edt"
url: "/mobilnisite/slovnik/cp-edt/"
type: "slovnik"
title: "CP-EDT – Control Plane Early Data Transmission"
date: 2025-01-01
abbr: "CP-EDT"
fullName: "Control Plane Early Data Transmission"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cp-edt/"
summary: "CP-EDT je mechanismus 3GPP umožňující přenos malých datových paketů přímo během úvodního procedury náhodného přístupu, bez zřizování plnohodnotného datového rádiového beareru. Výrazně snižuje signaliz"
---

CP-EDT je mechanismus 3GPP pro přenos malých datových paketů během úvodního procedury náhodného přístupu, který slouží ke snížení signalizace a spotřeby energie pro IoT zařízení, aniž by bylo nutné zřizovat plnohodnotný datový rádiový bearer.

## Popis

Control Plane Early Data Transmission (CP-EDT, časný přenos dat v řídicí rovině) je základní technologie pro hromadnou komunikaci strojového typu (mMTC) v sítích 5G a rozvinutých 4G. Zásadně mění způsob zpracování malých, občasných datových paketů tím, že umožňuje jejich přenos navázaný na signalizační zprávy řídicí roviny používané během úvodního navazování spojení, konkrétně během procedury náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)) a následné výměny signalizace nezávislé na přístupové vrstvě ([NAS](/mobilnisite/slovnik/nas/)). Tento přístup se vyhýbá tradičnímu a na zdroje náročnému procesu zřizování plnohodnotného datového rádiového beareru ([DRB](/mobilnisite/slovnik/drb/)), který zahrnuje více kroků signalizace řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), aktivaci zabezpečení a konfiguraci beareru.

Z architektonického hlediska CP-EDT funguje napříč uživatelským zařízením (UE), rádiovou přístupovou sítí (RAN - [eNB](/mobilnisite/slovnik/enb/)/gNB) a funkcí správy mobility v jádru sítě (Mobility Management Entity - [MME](/mobilnisite/slovnik/mme/) v 4G nebo Access and Mobility Management Function - [AMF](/mobilnisite/slovnik/amf/) v 5G). Procedura je zahájena, když má UE ve stavu RRC_IDLE nebo RRC_INACTIVE k odeslání malé množství dat v uplinku. UE indikuje svou schopnost a úmysl použít CP-EDT ve zprávě RRCConnectionResumeRequest nebo RRCConnectionRequest (prostřednictvím specifické příčiny navázání). Síť proceduru autorizuje na základě předplatitelských dat a síťových politik. Samotná uživatelská data jsou pak zapouzdřena v rámci NAS zprávy, konkrétně zprávy [UL](/mobilnisite/slovnik/ul/) NAS TRANSPORT, kterou RAN transparentně přenáší do jádra sítě.

Uzel jádra sítě (MME/AMF) extrahuje uživatelská data z NAS kontejneru a přepošle je příslušné funkci uživatelské roviny (UPF) nebo Serving Gateway (SGW) pro doručení na aplikační server. Pro datovou odpověď v downlinku může proces fungovat obráceně, přičemž jádro sítě vloží downlink paket do NAS zprávy (DL NAS TRANSPORT) odeslané ve zprávě RRCConnectionRelease, která převede UE zpět do stavu idle/inactive. Celá tato transakce je zabezpečena pomocí stávajícího NAS bezpečnostního kontextu (ochrana integrity a šifrování), což zajišťuje důvěrnost dat bez nutnosti zavádět samostatné zabezpečení přístupové vrstvy (AS). Klíčovým umožňovatelem je předem zřízený kontext UE uložený jak v RAN, tak v jádře sítě, který obsahuje potřebné bezpečnostní a kapacitní informace a umožňuje rychlé provedení procedury.

Úlohou CP-EDT je minimalizovat signalizační stopu a latenci pro sporadické přenosy dat. Je úzce spojen s funkcemi jako stav RRC Inactive a UE Assistance Information, kde může UE indikovat očekávaný vzorec datového provozu. RAN se rozhoduje, zda CP-EDT povolí, na základě faktorů jako velikost dat (s limitem maximální velikosti transportního bloku), rádiové podmínky a zatížení sítě. Tím, že integruje přenos dat do signalizace obnovení/navázání a uvolnění spojení, snižuje přibližně na polovinu počet potřebných signalizačních zpráv ve srovnání s konvenční procedurou služebního požadavku, což přináší přímé benefity v efektivitě sítě, výdrži baterie UE a využití prostředků rozhraní pro hromadné nasazení IoT, jak se předpokládá.

## K čemu slouží

CP-EDT byl vytvořen, aby řešil zásadní neefektivitu používání dědičných procedur spojení LTE/5G pro zařízení internetu věcí (IoT) a komunikace strojového typu (MTC). Tato zařízení, jako jsou senzory, měřiče a sledovače, typicky generují velmi malé datové přenosy (řádově desítky nebo stovky bajtů) v nepravidelných intervalech (např. hodinově nebo denně). Tradiční datový přenos iniciovaný mobilním zařízením vyžaduje, aby UE v idle režimu provedlo úplnou proceduru služebního požadavku: navázání RRC spojení, provedení NAS signalizace pro služební požadavek, aktivaci zabezpečení AS a zřízení alespoň jednoho datového rádiového beareru. Tento proces zahrnuje 10-15 signalizačních zpráv před odesláním prvního bitu aplikačních dat, což činí signalizační režii zcela nepoměrnou velikosti přenášených dat. To je plýtvání rádiovými zdroji, zvyšuje spotřebu energie UE a omezuje počet zařízení, které buňka může podporovat.

Historický kontext vychází z práce 3GPP na vylepšeních LTE pro MTC (eMTC) v Release 13 a následných verzích. Zatímco funkce jako Power Saving Mode (PSM) a Extended Discontinuous Reception (eDRX) byly vyvinuty ke snížení spotřeby energie zařízení v idle režimu, signalizační režie během aktivního přenosu zůstávala hlavním omezením. CP-EDT, zavedený v Release 15 jako část širšího rámce Early Data Transmission (EDT), přímo útočí na tento problém režie. Byl motivován potřebou podpory Massive IoT (mMTC) jako klíčového use case 5G, což vyžaduje, aby síť zvládla miliony nízkonákladových, energeticky efektivních zařízení na kilometr čtvereční.

CP-EDT problém řeší přizpůsobením řídicí roviny, která je inherentně optimalizována pro spolehlivý, bezpečný a efektivní přenos signalizace, pro přenos malých uživatelských datových paketů. To využívá stávající bezpečnostní a spolehlivostní mechanismy NAS signalizace. Řeší tak omezení předchozích přístupů, kde jedinou možností byla zdlouhavá cesta přes uživatelskou rovinu. Minimalizací času, po který je rádio aktivní, a snížením počtu zpracovatelských kroků vyžadovaných jak v UE, tak v síti, CP-EDT dramaticky prodlužuje výdrž baterie – často o roky u zařízení s dlouhými intervaly spánku – a zvyšuje kapacitu sítě pro IoT provoz, což umožňuje škálovatelné nasazení předpokládané pro chytrá města, utility a zemědělství.

## Klíčové vlastnosti

- Přenáší uživatelská data navázaná na NAS signalizační zprávy (UL/DL NAS TRANSPORT)
- Odstraňuje potřebu zřizovat datový rádiový bearer (DRB) pro malé pakety
- Využívá stávající NAS bezpečnostní kontext pro ochranu integrity a šifrování
- Je spouštěn prostřednictvím specifické příčiny navázání RRC (např. mo-Data, mo-ExceptionData, delayTolerant)
- Definuje limit maximální velikosti transportního bloku pro uplink data, která mají nárok na použití
- Podporuje transakční modely pouze pro uplink i pro uplink s downlink odpovědí

## Související pojmy

- [EDT – Energy Detection Threshold](/mobilnisite/slovnik/edt/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CP-EDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cp-edt/)
