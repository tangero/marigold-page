---
slug: "ra-sdt"
url: "/mobilnisite/slovnik/ra-sdt/"
type: "slovnik"
title: "RA-SDT – Random Access-based Small Data Transmission"
date: 2025-01-01
abbr: "RA-SDT"
fullName: "Random Access-based Small Data Transmission"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ra-sdt/"
summary: "RA-SDT je funkce 3GPP NR zavedená ve vydání 17, která umožňuje IoT a jiným zařízením přenášet malé datové pakety přímo během procedury náhodného přístupu, bez přechodu do plného stavu RRC Connected. T"
---

RA-SDT je funkce 3GPP NR, která umožňuje zařízením přenášet malé datové pakety přímo během procedury náhodného přístupu (Random Access), čímž se vyhne plnému připojovacímu stavu za účelem snížení signalizace a spotřeby energie.

## Popis

Random Access-based Small Data Transmission (RA-SDT, přenos malých dat založený na náhodném přístupu) je mechanismus definovaný ve vydání 3GPP 17 pro New Radio (NR), který umožňuje uživatelskému zařízení (UE), typicky IoT zařízení, přenést omezené množství dat ve směru uplink, zatímco zůstává ve stavu [RRC](/mobilnisite/slovnik/rrc/) Inactive. Využívá stávající proceduru fyzického kanálu pro náhodný přístup ([PRACH](/mobilnisite/slovnik/prach/)) jako nosiče pro jak přístupový požadavek, tak počáteční datový užitek. Základní myšlenkou je přenášet malé datové pakety v rámci zpráv procesu náhodného přístupu, čímž se vyhne rozsáhlé signalizační výměně potřebné k přechodu do stavu RRC Connected, provedení procedur služebního požadavku a následnému uvolnění spojení zpět do stavu inactive.

Z architektonického hlediska se RA-SDT integruje s procedurami náhodného přístupu s obsahem o 3 a 4 krocích definovanými pro NR. V přístupu se 3 kroky (MsgA) UE kombinuje tradiční preambuli (Msg1) a spojovací požadavek (Msg3) do jediného přenosu. RA-SDT může být implementován tím, že UE je umožněno zahrnout malý datový užitek do této MsgA. Odpověď gNB (MsgB) pak obsahuje nejen řešení kolizí a povolení pro uplink, ale také potvrzení přenesených dat. Pro přístup se 4 kroky mohou být data zahrnuta do Msg3. Klíčovými komponentami, které to umožňují, jsou vylepšení kontextu stavu RRC Inactive, který je uložen jak v UE, tak v síti (poslední obsluhující gNB a [AMF](/mobilnisite/slovnik/amf/)), což umožňuje gNB ověřit a zpracovat data bez plného nastavení RRC.

Jak to funguje, zahrnuje předkonfiguraci a přidělení zdrojů. Síť vysílá systémovou informaci oznamující podporu RA-SDT a jeho přidružené parametry, jako je maximální velikost transportního bloku pro data v MsgA/Msg3. UE ve stavu RRC Inactive s malým množstvím dat k odeslání a platným kontextem stavu Inactive může zahájit proceduru RA-SDT. Vybere odpovídající zdroj preambule nakonfigurovaný pro [SDT](/mobilnisite/slovnik/sdt/) a přenese MsgA (nebo Msg1) včetně dat. gNB, který rozpozná preambuli nebo obsah MsgA jako pokus o SDT, použije uložený kontext UE k ověření, dešifrování dat a jejich přeposlání do [UPF](/mobilnisite/slovnik/upf/) přes poslední obsluhující uzel NG-RAN. UE se pak může okamžitě po přijetí úspěšné MsgB (nebo Msg4) vrátit do stavu Inactive, čímž dokončí transakci s minimálními změnami stavu.

## K čemu slouží

RA-SDT byl vytvořen, aby řešil kritickou neefektivitu v scénářích celulárního IoT a hromadné komunikace strojového typu (mMTC): nepoměrně vysokou signalizační režii a spotřebu energie spojenou s přenosem velmi malých, občasných datových paketů. Tradiční procedury vyžadují kompletní nastavení a uvolnění spojení [RRC](/mobilnisite/slovnik/rrc/) i pro jediný datový paket, což může zahrnovat 10-20 signalizačních zpráv. Tato 'signalizační bouře' zahlcuje síť a vybíjí baterii omezených IoT zařízení, která jsou navržena na roky provozu na jedno nabití.

Motivace vychází z vývoje 5G směrem k podpoře širší škály případů užití, včetně ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a hromadného IoT. Před vydáním Rel-17 řešily podobné problémy mechanismy jako Early Data Transmission ([EDT](/mobilnisite/slovnik/edt/)) v LTE-M a NB-IoT, ale byly omezeny na tyto technologie. RA-SDT přináší tuto optimalizaci do hlavního spektra NR, což umožňuje efektivní podporu nové třídy zařízení NR-light (často nazývaných 'RedCap' – Reduced Capability). Řeší problém plýtvání síťovými zdroji a špatné životnosti baterie zařízení pro aplikace jako odečty senzorů, aktualizace chytrých měřidel nebo zdravotní monitory nositelných zařízení, které periodicky generují užitek o velikosti pouze několika bajtů.

Tím, že umožňuje přenos dat ve stavu RRC Inactive, RA-SDT přímo řeší omezení binárního modelu connected/inactive pro sporadický provoz. Snižuje latenci (vynecháním nastavení spojení), minimalizuje zatížení řídicí roviny na gNB a síti jádra a výrazně prodlužuje životnost baterie zařízení tím, že se vyhne operacím s vysokým výkonem spojeným s plnými připojovacími stavy. To činí z NR životaschopnější a efektivnější technologii pro rostoucí Internet věcí.

## Klíčové vlastnosti

- Umožňuje přenos dat ve směru uplink, zatímco UE zůstává ve stavu RRC Inactive, a vyhne se tak přechodu do stavu RRC Connected.
- Využívá proceduru náhodného přístupu se 3 kroky (MsgA) nebo se 4 kroky (Msg3) k přenosu malých datových užitečných zatížení.
- Předkonfigurováno pomocí systémové informace s parametry jako maximální velikost transportního bloku pro SDT.
- Spoléhá se na uložený kontext UE Inactive v gNB a síti jádra pro ověření a přeposlání dat.
- Výrazně snižuje signalizační režii, latenci a spotřebu energie UE pro sporadická malá data.
- Zavedeno jako součást vylepšení 5G NR pro IoT a zařízení s redukovanými schopnostmi (RedCap) ve vydání Rel-17.

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [RA-SDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ra-sdt/)
