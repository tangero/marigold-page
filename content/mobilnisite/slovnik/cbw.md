---
slug: "cbw"
url: "/mobilnisite/slovnik/cbw/"
type: "slovnik"
title: "CBW – Carrier Bandwidth"
date: 2025-01-01
abbr: "CBW"
fullName: "Carrier Bandwidth"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbw/"
summary: "Carrier Bandwidth (CBW) označuje celkové frekvenční spektrum přidělené jednomu nosnému signálu (carrier) v mobilních sítích. Určuje maximální kapacitu pro přenos dat a dostupnou šířku kanálu pro komun"
---

CBW je celkové frekvenční spektrum přidělené jednomu nosnému signálu (carrier) v mobilní síti, které určuje jeho maximální datovou kapacitu a šířku kanálu pro komunikaci.

## Popis

Carrier Bandwidth (CBW) představuje základní frekvenční zdroj přidělený jednomu nosnému signálu (carrier) v systémech mobilní komunikace a definuje celkovou šířku spektra dostupnou pro vysílací a přijímací operace. Ve specifikacích 3GPP je CBW kritickým parametrem, který přímo ovlivňuje výkon systému, kapacitu a flexibilitu nasazení napříč různými rádiovými přístupovými technologiemi včetně LTE a NR. Šířka pásma se typicky měří v megahertzech (MHz) a určuje maximální dosažitelné datové rychlosti, kapacitu kanálu a spektrální účinnost pro daný konkrétní nosný signál.

Z architektonického hlediska je CBW implementována jak na fyzické vrstvě, tak na vyšších protokolových vrstvách v rámci rádiové přístupové sítě (RAN). Na fyzické vrstvě šířka pásma definuje počet dostupných subnosných v systémech založených na [OFDM](/mobilnisite/slovnik/ofdm/), přičemž každá subnosná zabírá konkrétní frekvenční zdrojový element. Základnová stanice (eNodeB v LTE, gNB v NR) konfiguruje parametry CBW prostřednictvím systémových informačních bloků a vyhrazených signalizačních zpráv, čímž zajišťuje správné sladění mezi síťovou infrastrukturou a schopnostmi uživatelského zařízení (UE). Tato konfigurace zahrnuje nejen celkovou šířku pásma, ale také konkrétní frekvenční alokaci v rámci licencovaného pásma.

Z pohledu protokolů jsou parametry CBW komunikovány prostřednictvím různých specifikací 3GPP, včetně TS 36.104 pro LTE a TS 38.104 pro NR, které definují šířky kanálového pásma a konfigurace přenosového pásma. Konfigurace šířky pásma ovlivňuje více aspektů systému, včetně počtu dostupných bloků fyzických zdrojů (PRB), vzorů referenčních signálů, umístění synchronizačních signálů a alokace řídicích kanálů. Pro různé scénáře nasazení jsou definovány různé třídy šířky pásma, od úzkopásmových implementací pro IoT aplikace až po širokopásmové konfigurace pro rozšířené služby mobilního širokopásmového přístupu (eMBB).

Implementace CBW zahrnuje sofistikované algoritmy správy rádiových zdrojů, které dynamicky přidělují spektrální zdroje na základě požadavků provozu, podmínek interference a požadavků na kvalitu služby (QoS). Operátoři sítí mohou konfigurovat více nosných signálů s různými šířkami pásma za účelem vytvoření scénářů agregace nosných ([CA](/mobilnisite/slovnik/ca/)), kde se kombinuje více instancí CBW, aby poskytly širší efektivní šířku pásma a vyšší datové rychlosti. Tato schopnost je obzvláště důležitá pro nasazení 5G NR, kde flexibilní konfigurace šířky pásma podporují rozmanité případy užití včetně masivního IoT (mIoT), ultra-spolehlivé komunikace s nízkou latencí (URLLC) a rozšířených služeb mobilního širokopásmového přístupu (eMBB) napříč různými frekvenčními rozsahy.

## K čemu slouží

Carrier Bandwidth existuje jako základní koncept v mobilních sítích za účelem efektivního řízení a alokace omezených spektrálních zdrojů mezi více uživateli a službami. Primárním účelem je definovat přenosovou kapacitu jednotlivých rádiových nosných signálů (carrier), což umožňuje síťovým operátorům optimalizovat využití spektra při současném splnění různorodých požadavků služeb. Bez standardizovaných definic CBW by byla nemožná interoperabilita mezi síťovými zařízeními a uživatelskými terminály, což by vedlo k neefektivnímu využití spektra a degradaci výkonu systému.

Historicky rané mobilní systémy používaly pevné alokace šířky pásma, které omezovaly flexibilitu nasazení a spektrální účinnost. Evoluce směrem ke standardům 3GPP přinesla sofistikovanější schopnosti správy šířky pásma, umožňující dynamickou alokaci a konfiguraci na základě požadavků služeb a scénářů nasazení. Tato evoluce řešila omezení předchozích přístupů tím, že umožnila škálovatelné konfigurace šířky pásma, které se dokážou přizpůsobit proměnlivým vzorcům provozu, hustotě uživatelů a požadavkům služeb v různých geografických oblastech a scénářích nasazení sítě.

Vytvoření standardizovaných parametrů CBW bylo motivováno potřebou podporovat stále rozmanitější případy užití při zachování zpětné kompatibility a efektivního využití spektra. Jak se mobilní sítě vyvíjely z hlasově orientovaných systémů na datově intenzivní platformy podporující multimediální služby, IoT aplikace a komunikace pro klíčové mise, flexibilní konfigurace šířky pásma se staly nezbytnými pro optimalizaci výkonu sítě napříč různými frekvenčními pásmy a prostředími nasazení. Standardizace CBW umožňuje síťovým operátorům nasazovat nákladově efektivní řešení, která maximalizují spektrální účinnost a zároveň podporují požadavky na kvalitu služby (QoS) moderních mobilních služeb.

## Klíčové vlastnosti

- Definuje celkové frekvenční spektrum přidělené na jeden nosný signál (carrier)
- Určuje maximální dosažitelné datové rychlosti a kapacitu
- Konfigurovatelná napříč různými frekvenčními pásmy a scénáři nasazení
- Podporuje agregaci nosných (CA) pro širší efektivní šířku pásma
- Umožňuje flexibilní využití spektra pro různé služby
- Standardizována ve specifikacích 3GPP pro zajištění interoperability

## Definující specifikace

- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TR 37.829** (Rel-18) — Technical Report
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TS 38.819** (Rel-16) — Band n65 for New Radio Technical Report
- **TR 38.828** (Rel-16) — CLI and RIM for NR
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.844** (Rel-18) — Efficient utilization of licensed spectrum
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [CBW na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbw/)
