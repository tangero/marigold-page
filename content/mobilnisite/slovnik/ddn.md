---
slug: "ddn"
url: "/mobilnisite/slovnik/ddn/"
type: "slovnik"
title: "DDN – Downlink Data Notification"
date: 2025-01-01
abbr: "DDN"
fullName: "Downlink Data Notification"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ddn/"
summary: "Downlink Data Notification (DDN) je signalizační zpráva používaná Serving Gateway (SGW) k informování MME/SGSN, že pro UE ve stavu ECM-IDLE nebo PMM-IDLE dorazila data pro downlink. Spouští proceduru"
---

DDN je signalizační zpráva od Serving Gateway, která informuje MME/SGSN o doručených datových paketech pro pro downlink pro neaktivní (idle) UE a spouští proceduru pagingu a obnovení přenosového kanálu (bearer).

## Popis

Downlink Data Notification (DDN) je klíčová procedura řídicí roviny v rámci architektur 3GPP Evolved Packet Core (EPC) a 5G Core (5GC). Funguje, když je User Equipment (UE) v neaktivním stavu (idle) – konkrétně ECM-IDLE v LTE/EPC nebo CM-IDLE v 5G/5GC. V tomto stavu je rádiové spojení UE uvolněno pro úsporu baterie a síť udržuje kontext UE pouze na úrovni core networku (např. v [MME](/mobilnisite/slovnik/mme/) nebo [AMF](/mobilnisite/slovnik/amf/)). Když pakety dat pro downlink dorazí z Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)) Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) na Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a odpovídající UE je neaktivní, SGW nemůže data přeposlat, protože přenosové kanály (user plane bearers) jsou neaktivní. SGW proto musí signalizovat Mobility Management Entity (MME) v 4G nebo Access and Mobility Management Function (AMF) v 5G, aby iniciovalo obnovení těchto kanálů.

Zpráva DDN je odesílána ze SGW na MME přes rozhraní S11 v 4G nebo ze SMF na AMF přes rozhraní N11 v 5G. Tato zpráva obsahuje identifikátory, jako je EPS Bearer ID nebo [PDU](/mobilnisite/slovnik/pdu/) Session ID a IP adresu UE, pro jednoznačnou identifikaci relace, pro kterou jsou data čekající. Po přijetí DDN MME/AMF zkontroluje mobilitu UE a kontext předplatného. Pokud je UE oprávněno k zavolání (paging) a je registrováno v oblasti sledování (tracking area), MME/AMF spustí proceduru služebního požadavku iniciovanou sítí. To zahrnuje odeslání zprávy pro zavolání (paging message) na všechny evolved NodeBs (eNBs) nebo gNBs v registrované oblasti sledování UE, aby bylo UE lokalizováno a přešlo do připojeného stavu (ECM-CONNECTED nebo CM-CONNECTED).

Jakmile UE odpoví na zavolání (page) a provede proceduru náhodného přístupu (random access), MME/AMF koordinuje se SGW a eNB/gNB obnovení pozastavených přenosových kanálů (user plane bearers) nebo zdrojů PDU relace. To zahrnuje vytvoření S1-U nebo N3 tunelu uživatelské roviny mezi eNB/gNB a SGW/UPF. Teprve po dokončení tohoto obnovení přenosových kanálů SGW přepošle data pro downlink, která měla v bufferu, na eNB/gNB pro přenos na UE. Mechanismus DDN je úzce integrován s dalšími funkcemi core networku, jako je Home Subscriber Server (HSS) nebo Unified Data Management (UDM) pro ověření předplatného, a s řízením politik přes Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF), aby bylo zajištěno uplatnění QoS politik během reaktivace přenosových kanálů.

V architektonickém vývoji směrem k 5G, zatímco základní koncept zůstává, detaily implementace se mění. V 5GC může SMF (která kombinuje některé řídicí rovinné funkce SGW) spustit notifikaci směrem k AMF, analogickou DDN, když data pro downlink dorazí na UPF pro neaktivní UE. Systém 5GC používá pro tuto signalizaci SMF-AMF rozhraní N11. Dále vylepšení v 5G, jako je podpora síťového řezání (network slicing) a podrobnější režimy šetření energie, ovlivňují, jak a kdy jsou notifikace typu DDN generovány a zpracovávány, aby byly v souladu s charakteristikami řezů a preferencemi UE pro šetření energie.

## K čemu slouží

Mechanismus Downlink Data Notification byl vytvořen k vyřešení základního konfliktu v návrhu mobilních sítí: umožnit User Equipment (UE) šetřit energii baterie přechodem do neaktivních stavů (idle) bez aktivního rádiového spojení, a zároveň zajistit, aby síť mohla doručit data pro downlink na UE s minimálním zpožděním, když taková data dorazí. Bez DDN by síť musela buď udržovat UE v připojeném stavu (connected) nepřetržitě – což by rychle vybíjelo jejich baterie – nebo riskovat ztrátu dat pro downlink, protože síť by neměla způsob, jak lokalizovat a probudit neaktivní UE, když pro něj data čekají.

Historicky, v před-3GPP paketových systémech, existovaly podobné mechanismy, ale byly méně optimalizované. DDN, jak je standardizováno v 3GPP, poskytuje standardizovanou, efektivní a škálovatelnou signalizační proceduru mezi gateway uzly (SGW, SMF) a uzly správy mobility (MME, AMF). Řeší omezení dřívějších přístupů oddělením detekce v datové rovině (na gateway) od řízení mobility a volání (paging) (na MME/AMF), což umožňuje specializované síťové funkce a optimalizované signalizační toky. Toto oddělení je klíčovým principem architektur EPC a 5GC.

Vytvoření a zdokonalení DDN bylo motivováno exponenciálním růstem mobilního datového provozu a neustále připojenými aplikacemi (jako push e-mail, instant messaging a příkazy pro IoT senzory), které generují sporadická data pro downlink. DDN zajišťuje, že tyto aplikace fungují bezproblémově, aniž by vyžadovaly neustálé připojení UE. Je to základní kámen pro umožnění pokročilých funkcí šetření energie, jako je Power Saving Mode (PSM) a extended Discontinuous Reception (eDRX), protože poskytuje garantovaný probouzející mechanismus, který síť potřebuje k dosažení UE. V podstatě DDN činí kompromis mezi energetickou účinností UE a dosažitelností ze sítě zvládnutelným a spolehlivým.

## Klíčové vlastnosti

- Spouští proceduru služebního požadavku iniciovanou sítí (network-initiated service request) pro neaktivní (idle) UE
- Signalizuje z gateway uživatelské roviny (SGW/UPF-SMF) ke správci mobility (MME/AMF)
- Využívá rozhraní S11 v 4G/EPC a rozhraní N11 v 5G/5GC
- Obsahuje identifikátory pro konkrétní přenosový kanál (bearer) nebo PDU relaci s čekajícími daty
- Iniciuje zavolání (paging) za účelem lokalizace UE v její registrované oblasti sledování/směrování (tracking/routing area)
- Umožňuje obnovení pozastavených tunelů uživatelské roviny před přeposláním dat

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)

## Definující specifikace

- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service

---

📖 **Anglický originál a plná specifikace:** [DDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ddn/)
