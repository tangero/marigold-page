---
slug: "csma-ca"
url: "/mobilnisite/slovnik/csma-ca/"
type: "slovnik"
title: "CSMA/CA – Carrier Sense Multiple Access with Collision Avoidance"
date: 2025-01-01
abbr: "CSMA/CA"
fullName: "Carrier Sense Multiple Access with Collision Avoidance"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/csma-ca/"
summary: "CSMA/CA je protokol řízení přístupu k médiu (MAC) používaný v bezdrátových sítích pro správu sdílení komunikačního kanálu zařízeními. Zabraňuje kolizím dat tím, že zařízení před vysíláním naslouchají"
---

CSMA/CA je protokol řízení přístupu k médiu používaný v bezdrátových sítích, kde zařízení před vysíláním naslouchají kanálu a využívají náhodné časovače odkladu, aby se vyhnula kolizím dat. Je klíčový pro provoz v neregulovaném spektru, jako je Wi-Fi a 3GPP NR-U.

## Popis

Carrier Sense [Multiple Access](/mobilnisite/slovnik/multiple-access/) with Collision Avoidance (CSMA/[CA](/mobilnisite/slovnik/ca/)) je základní protokol v rámci vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), navržený speciálně pro sdílená, konkurenční bezdrátová prostředí, kde je dostupný fyzický mechanismus snímání nosné, ale detekce kolizí je nepraktická. Na rozdíl od svého drátového protějšku [CSMA/CD](/mobilnisite/slovnik/csma-cd/) (Collision Detection) CSMA/CA předchází kolizím paketů namísto jejich následného řešení, což je v bezdrátových systémech zásadní kvůli problému skrytého uzlu a neschopnosti vysílače spolehlivě detekovat kolizi během vysílání. Protokol funguje na principu 'naslouchat před vysíláním' ([LBT](/mobilnisite/slovnik/lbt/)), který ukládá zařízení povinnost nejprve vysnímat rádiový kanál, aby zjistilo, zda je volný, než zahájí přenos. Pokud je kanál obsazený, zařízení přenos odloží a vstoupí do procedury odkladu.

Základní operační sekvence CSMA/CA zahrnuje několik klíčových kroků. Nejprve zařízení provede vyhodnocení volného kanálu ([CCA](/mobilnisite/slovnik/cca/)) měřením energie na kanále. Pokud je kanál vysnímán jako volný po stanovenou dobu (např. Distributed Inter-Frame Space, DIFS), může zařízení pokračovat. Aby se však dále minimalizovala šance, že více zařízení začne vysílat současně po skončení obsazeného období, je použit náhodný časovač odkladu. Zařízení vybere náhodný počet časových slotů v rámci 'konkurenčního okna' a tento časovač odpočítává pouze tehdy, pokud kanál zůstává volný. K vysílání dojde, jakmile časovač dosáhne nuly. Pokud se kanál během odpočtu časovače obsadí, časovač se pozastaví a pokračuje až poté, co je kanál opět volný po požadovanou dobu. Tento mechanismus odkladu statisticky rozprostírá pokusy o přenos, čímž snižuje pravděpodobnost kolizí.

Pro spolehlivý provoz je CSMA/CA často spojován se schématem kladného potvrzení. Po úspěšném přijetí datového rámče přijímací zařízení okamžitě odešle vysílači zpět potvrzovací ([ACK](/mobilnisite/slovnik/ack/)) rámec. Pokud vysílač neobdrží ACK v rámci časového limitu, předpokládá, že došlo ke kolizi nebo chybě, a naplánuje opakovaný přenos, přičemž pro další pokus exponenciálně zvětší velikost svého konkurenčního okna (proces známý jako binární exponenciální odklad). Tento adaptivní odklad pomáhá zvládat zahlcení sítě. V kontextech 3GPP, zejména pro New Radio v neregulovaném spektru ([NR-U](/mobilnisite/slovnik/nr-u/)) specifikované od Release 13, je CSMA/CA založené LBT v mnoha regionech (např. Evropa, Japonsko) regulatorním požadavkem pro zajištění spravedlivé koexistence s jinými systémy, jako je Wi-Fi, v pásmech 5 GHz a 6 GHz. Implementační detaily 3GPP, včetně tříd priority přístupu ke kanálu, dob snímání a maximálních dob obsazenosti kanálu, jsou pečlivě definovány tak, aby splňovaly jak regulatorní požadavky, tak i výkonnostní cíle 5G.

## K čemu slouží

CSMA/CA byl vytvořen, aby vyřešil základní problém více nekoordinovaných zařízení soutěžících o přístup ke sdílenému bezdrátovému médiu, kde klasická metoda detekce kolizí používaná v Ethernetu (CSMA/CD) selhává. V bezdrátové komunikaci vysílající zařízení nemůže spolehlivě naslouchat kolizím na stejném kanále, který používá k vysílání, kvůli velkému rozdílu ve výkonu mezi jeho vlastním přenosem a potenciálně slabým příchozím signálem ze vzdáleného kolizního vysílače. Toto omezení v kombinaci s problémem 'skrytého uzlu' – kdy se dvě zařízení navzájem neslyší, ale obě mohou rušit společného přijímače – činí proaktivní předcházení kolizím nezbytným pro efektivní využití kanálu.

Vývoj protokolu byl hnán potřebou decentralizovaného, distribuovaného přístupu v neregulovaných kmitočtových pásmech, nejvýznamněji pro sítě IEEE 802.11 (Wi-Fi). Jeho účelem je poskytnout spravedlivou a statisticky efektivní metodu pro sdílení kanálu zařízeními bez nutnosti centrálního plánovače nebo explicitní časové synchronizace, což by přidalo značnou režii a složitost. Vynucením disciplíny naslouchání před vysíláním a zahrnutím náhodných odkladů CSMA/CA minimalizuje období destruktivního rušení (kolizí), čímž ve srovnání s jednoduššími, čistě ALOHA stylovými přístupovými metodami zvyšuje celkovou propustnost a spolehlivost bezdrátové sítě.

3GPP přijalo a specifikovalo mechanismy CSMA/CA počínaje Release 13, primárně aby umožnilo celulárním technologiím, jako je LTE-LAA (License Assisted Access) a následně NR-U, fungovat v neregulovaném spektru. Účel je zde dvojí: splnit přísné regionální regulatorní požadavky na spravedlivou koexistenci se stávajícími systémy (zejména Wi-Fi) a umožnit systémům 3GPP využít dodatečnou šířku pásma pro zvýšení kapacity. Integrací CSMA/CA zajišťuje 3GPP, že jeho nasazení jsou dobrými sousedy ve sdíleném spektru, a vyhýbá se tak vytvoření dominantní, nekooperativní technologie, která by degradovala výkon všech ostatních uživatelů. Toto přijetí bylo motivováno potřebou průmyslu po větším množství spektra a úspěchem principu LBT při umožnění koexistence heterogenních technologií.

## Klíčové vlastnosti

- Snímání kanálu metodou Naslouchat před vysíláním (LBT) prostřednictvím vyhodnocení volného kanálu (CCA)
- Náhodný časovač odkladu s konkurenčním oknem pro rozestavení přenosů
- Binární exponenciální odklad pro opakované přenosy pro adaptaci na zahlcení
- Schéma kladného potvrzení (ACK) pro spolehlivé doručování rámců
- Třídy priority přístupu ke kanálu definující různé doby snímání a obsazenosti (v 3GPP NR-U)
- Podpora koexistence s jinými rádiovými přístupovými technologiemi v neregulovaných pásmech

## Související pojmy

- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TS 28.403** (Rel-19) — WLAN Performance Measurements

---

📖 **Anglický originál a plná specifikace:** [CSMA/CA na 3GPP Explorer](https://3gpp-explorer.com/glossary/csma-ca/)
