---
slug: "dvb-t-t2"
url: "/mobilnisite/slovnik/dvb-t-t2/"
type: "slovnik"
title: "DVB-T/T2 – Digital Video Broadcasting - Terrestrial / Terrestrial Second Generation"
date: 2025-01-01
abbr: "DVB-T/T2"
fullName: "Digital Video Broadcasting - Terrestrial / Terrestrial Second Generation"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dvb-t-t2/"
summary: "DVB-T/T2 označuje standardy pro digitální vysílání v pozemní televizi (Digital Video Broadcasting), které 3GPP přijalo pro doručování služby MBMS. Umožňuje efektivní vysílání multimediálního obsahu do"
---

DVB-T/T2 je standard pro digitální vysílání v pozemní televizi (Digital Video Broadcasting) přijatý 3GPP, který umožňuje efektivní vysílání multimediálního obsahu do mobilních zařízení v rámci architektury MBMS.

## Popis

[DVB-T](/mobilnisite/slovnik/dvb-t/)/[T2](/mobilnisite/slovnik/t2/) v kontextu 3GPP představuje přijetí zavedených standardů pro pozemní vysílání do architektury služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), konkrétně pro její rozšířenou verzi (eMBMS). Architektura zahrnuje Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), které slouží jako vstupní bod pro poskytovatele obsahu a komunikuje s vysílací sítí LTE nebo 5G NR. Komponenty jádra sítě, jako je MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a Multicell Coordination Entity ([MCE](/mobilnisite/slovnik/mce/)), připravují a plánují vysílací provoz. Přístupová síť využívá provoz v jedné frekvenční síti (Single Frequency Network, [SFN](/mobilnisite/slovnik/sfn/)), kdy více buněk synchronně vysílá identické signály, což umožňuje uživatelskému zařízení (UE) je kombinovat jako vícecestný příjem, což výrazně zlepšuje pokrytí a spektrální účinnost pro vysílací služby.

Technický provoz zahrnuje přijímání IP multicast paketů s mediálním obsahem BM-SC. Tyto pakety jsou zpracovány a jsou generovány oznámení služby. MBMS-GW zajišťuje přeposílání paketů v uživatelské rovině a správu relací v řídicí rovině, čímž zahajuje MBMS relaci. MCE je zodpovědná za přidělování rádiových zdrojů a jejich plánování napříč více [eNB](/mobilnisite/slovnik/enb/) nebo gNB, čímž zajišťuje synchronizovaný přenos v oblasti MBSFN. Na rádiovém rozhraní je obsah namapován na Physical Multicast Channel (PMCH) v LTE nebo na Physical Downlink Shared Channel (PDSCH) se specifickým plánováním pro vysílání v 5G NR. Uživatelské zařízení (UE) využívá speciální příjmový režim k dekódování těchto vysílacích signálů.

Klíčové komponenty zahrnují BM-SC pro poskytování služeb a zabezpečení, MBMS-GW pro distribuci IP multicastu v jádru sítě a MCE pro synchronizovanou správu rádiových zdrojů. Uživatelské zařízení (UE) musí podporovat příslušné schopnosti pro příjem MBMS. Protokolový zásobník zahrnuje SYNC protokol pro doručování časových informací k eNB/gNB a aplikační vrstvou Forward Error Correction (FEC) pro robustní doručování. Jeho úlohou je poskytovat vysokoúčinnou vysílací vrstvu s širokým pokrytím v rámci mobilní sítě, která je oddělena od individuálních unicastových spojení, a je tak ideální pro lineární televizi, živé události a aktualizace softwaru.

## K čemu slouží

Účelem integrace standardů DVB-T/T2 do 3GPP bylo využít zralé, vysoce účinné vysílací technologie pro doručování multimédií do mobilních zařízení. Tím se řešil problém neefektivního doručování oblíbeného obsahu v reálném čase (jako sport nebo zprávy) pomocí unicastu, který při současném požadavku mnoha uživatelů na stejný stream nadměrně spotřebovává rádiové zdroje a zdroje jádra sítě. Přijetím těchto prověřených fyzických vrstev pro vysílání mohlo 3GPP nabídnout komplementární vysílací režim, který se dokonale škáluje s velikostí publika a využívá konstantní množství šířky pásma bez ohledu na počet přijímačů.

Historicky byly mobilní sítě navrženy primárně pro obousměrnou unicastovou komunikaci. Vytvoření MBMS v dřívějších releasích sice zavedlo multicast/vysílání, ale původně používalo vlnové formy specifické pro buněčné sítě. Přijetí DVB-T2 v Release 14 bylo motivováno jeho vyšší spektrální účinností a robustností ve srovnání s dřívějšími vlnovými formami eMBMS založenými na LTE. DVB-T2 nabízí pokročilé kódování a modulaci (jako 256-QAM), účinnější FEC (BCH+LDPC) a flexibilní parametry OFDM, což umožňuje vyšší datové rychlosti a lepší výkon v náročných příjmových podmínkách. Tato integrace vyřešila omezení v podobě nízké vysílací kapacity a pokrytí v čistě buněčných vysílacích režimech a poskytla konkurenceschopnou alternativu k tradičním televizním vysílacím sítím pro mobilní příjem.

## Klíčové vlastnosti

- Vysoká spektrální účinnost využívající modulační a kódovací schémata DVB-T2 (např. 256-QAM, LDPC/BCH FEC)
- Podpora provozu v jedné frekvenční síti (Single Frequency Network, SFN) pro širokoplošné pokrytí a odolnost vůči rušení
- Integrace s 3GPP MBMS služební vrstvou pro autentizaci, oznamování služeb a účtování
- Flexibilní konfigurace fyzické vrstvy (velikost FFT, ochranný interval) pro přizpůsobení různým kanálovým podmínkám
- Efektivní doručování IP datagramů pro vysílací/multicastový obsah přes pozemní rádiové rozhraní
- Komplementární využití spolu s unicastovým LTE/5G NR pro hybridní doručování služeb

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [DVB-T/T2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/dvb-t-t2/)
