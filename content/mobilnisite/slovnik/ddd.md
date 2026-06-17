---
slug: "ddd"
url: "/mobilnisite/slovnik/ddd/"
type: "slovnik"
title: "DDD – Downlink Data Delivery"
date: 2025-01-01
abbr: "DDD"
fullName: "Downlink Data Delivery"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ddd/"
summary: "Downlink Data Delivery (DDD) je mechanismus 3GPP, který umožňuje efektivní doručování dat ve směru downlink (směrem k uživatelskému zařízení) uživatelskému zařízení (UE) v úsporných stavech, zejména k"
---

DDD je mechanismus 3GPP pro efektivní doručování dat ve směru downlink (směrem k uživatelskému zařízení) uživatelskému zařízení (UE) v úsporných stavech, jako je RRC_INACTIVE nebo RRC_IDLE, který optimalizuje využití prostředků snížením signalizační režie a latence.

## Popis

Downlink Data Delivery (DDD) je sofistikovaný mechanismus definovaný v architektuře 5G Core Network (5GC), konkrétně v kontextech Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Jeho hlavní funkcí je řídit efektivní doručování paketů dat ve směru downlink (směrem k uživatelskému zařízení) k UE, které není v aktivním stavu připojení Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) (tj. RRC_CONNECTED). Když UE přejde do stavů RRC_INACTIVE nebo RRC_IDLE pro úsporu baterie, Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a SMF koordinují udržování kontextu protokolové datové jednotky (PDU) relace UE. UPF ukládá do vyrovnávací paměti příchozí pakety downlinkových dat určené pro neaktivní UE. Poté je spuštěn postup DDD, který zahrnuje iniciování síťově spouštěné žádosti o službu ze strany sítě pro vyvolání (paging) UE a znovunavázání cesty uživatelské roviny.

Architektura zahrnuje úzkou interakci mezi SMF, AMF, UPF a Radio Access Network (RAN). SMF, jako centrální kontrolér pro PDU relace, je zodpovědná za určení politik DDD a za instruování UPF. UPF funguje jako kotvící bod, detekuje příchod downlinkových dat pro pozastavenou PDU relaci a ukládá pakety do vyrovnávací paměti. Poté o tom informuje SMF prostřednictvím N4 session report. Po obdržení tohoto oznámení SMF vyhodnotí, zda spustit postup DDD. Pokud je spuštěn, SMF odešle požadavek Namf_Communication_N1N2MessageTransfer na AMF, který obsahuje potřebnou signalizaci [NAS](/mobilnisite/slovnik/nas/) k předání UE a instrukce pro RAN. AMF poté iniciuje vyvolání (paging) pro lokalizaci UE a znovunavázání RRC spojení.

Postup funguje využitím registrační oblasti UE a možností vyvolání (paging). Jakmile UE odpoví na vyvolání, RAN naváže RRC spojení a přepošle zprávu NAS od SMF. Tato zpráva vyzve UE k zahájení postupu žádosti o službu. Následně je znovu aktivována cesta uživatelské roviny mezi UPF a RAN a data uložená ve vyrovnávací paměti jsou doručena UE. Mezi klíčové komponenty patří schopnost ukládání do vyrovnávací paměti v UPF, mechanismus hlášení událostí na rozhraní N4 a koordinace postupu žádosti o službu mezi SMF a AMF prostřednictvím rozhraní N11/Namf.

Role DDD v síti je klíčová pro vyvážení spotřeby energie UE s dosažitelností v síti. Minimalizuje potřebu, aby se UE periodicky probouzela a dotazovala na data, čímž prodlužuje životnost baterie pro zařízení IoT a mobilní zařízení. Ukládáním dat do vyrovnávací paměti v UPF a spouštěním znovunavázání spojení pouze při dostupnosti dat snižuje zbytečnou signalizaci přes rádiové rozhraní a v jádru sítě. To činí síť škálovatelnější a efektivnější, zejména pro scénáře massive Machine-Type Communication (mMTC) definované v 5G.

## K čemu slouží

DDD byl vytvořen, aby řešil kritickou výzvu doručování downlinkových dat (dat směrem k uživatelskému zařízení) k UE v úsporných stavech bez kompromisů v životnosti baterie. V předchozích generacích mobilních sítí muselo UE v režimu idle periodicky naslouchat zprávám pro vyvolání (paging) nebo přecházet do připojeného stavu, aby zkontrolovalo data, což spotřebovávalo značnou energii. Pro IoT aplikace s nepravidelnými downlinkovými příkazy nebo aktualizacemi to bylo velmi neefektivní. DDD to řeší tím, že umožňuje síti data uchovávat a inteligentně probouzet UE pouze při skutečné dostupnosti dat k doručení, čímž řeší problém downlinkové dosažitelnosti pro zařízení s omezeným příkonem.

Motivace vychází z požadavku 5G podporovat massive IoT s ultra nízkou spotřebou energie. Tradiční přístupy vyžadovaly buď udržování UE v připojeném stavu (vysoký odběr energie), nebo spoléhání se na dlouhé cykly nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)) v režimu idle (způsobující vysokou downlinkovou latenci). DDD poskytuje optimalizovaný střední přístup. Byl zaveden jako součást nativní podpory stavu [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE v systému 5G, který nabízí rychlé obnovení spojení s uloženým kontextem. DDD využívá tento stav k minimalizaci signalizace a zpoždění ve srovnání s úplným přechodem z idle do aktivního stavu, čímž řeší omezení dřívějších systémů, kde příchod downlinkových dat často spouštěl zdlouhavý postup zřizování služby.

Historicky, v 4G EPS, existoval podobný koncept nazývaný Downlink Data Notification ([DDN](/mobilnisite/slovnik/ddn/)) od Serving Gateway (SGW) k MME. DDD v 5G je však více integrovaný a optimalizovaný. Je navržen pro servisně orientovanou architekturu 5GC s jasnějším oddělením řídicích a uživatelských funkcí. Bezproblémově spolupracuje se stavem RRC_INACTIVE zavedeným v 5G NR, který v LTE nebyl dostupný. To umožňuje rychlejší přechody stavů a efektivnější využití prostředků, naplňující cíle 5G v oblasti síťové efektivity a podpory různorodých požadavků služeb.

## Klíčové vlastnosti

- Efektivní ukládání downlinkových datových paketů do vyrovnávací paměti v UPF pro UE v neaktivních/idle stavech
- Spouštění síťově iniciovaného postupu žádosti o službu prostřednictvím interakce SMF-AMF
- Snížení spotřeby energie UE minimalizací zbytečných probuzení
- Optimalizace signalizační režie na rádiových rozhraních a rozhraních jádra sítě
- Podpora doručování downlinku s nízkou latencí, když je kontext UE uložen ve stavu RRC_INACTIVE
- Bezproblémová integrace s servisně orientovanými rozhraními 5G core (N4, N11, Namf)

## Definující specifikace

- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service

---

📖 **Anglický originál a plná specifikace:** [DDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ddd/)
