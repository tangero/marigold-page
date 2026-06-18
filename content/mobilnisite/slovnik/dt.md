---
slug: "dt"
url: "/mobilnisite/slovnik/dt/"
type: "slovnik"
title: "DT – Data Termination"
date: 2026-01-01
abbr: "DT"
fullName: "Data Termination"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/dt/"
summary: "Data Termination (DT) je síťová schopnost nebo funkční entita, která poskytuje ukončovací bod pro paketové datové spojení, zajišťuje finální směrování a doručení uživatelských dat k cílové aplikaci ne"
---

DT je síťová funkce, která ukončuje paketové datové spojení a zajišťuje finální směrování a doručení uživatelských dat k aplikaci nebo koncovému bodu služby uvnitř nebo vně sítě.

## Popis

Data Termination (DT) v terminologii 3GPP označuje logickou funkci nebo síťovou entitu, která slouží jako koncový bod pro paketovou datovou relaci uživatele. Je to místo, kde je ukotvena datová cesta uživatelské roviny a kde dochází k finálnímu zpracování a přeposílání IP paketů k jejich cíli. Funkce DT může být umístěna v různých síťových prvcích v závislosti na architektuře, například v bráně paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/)) v 4G EPC, ve funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5GC nebo na konkrétním serveru poskytujícím službu. Jejím hlavním úkolem je spravovat ukončení přenosového kanálu nebo QoS toku, který nese data uživatele, což zahrnuje úkoly jako přidělování IP adres, směrování provozu, vynucování politik a generování účtovacích dat.

Architektonicky se DT nachází na rozhraní mezi jádrovou sítí mobilního operátora a externí paketovou datovou sítí ([PDN](/mobilnisite/slovnik/pdn/)), jako je internet nebo síť IMS. V Evolved Packet Core (EPC) funkci DT plní PGW tím, že poskytuje UE přístup k PDN. Vytváří [GTP](/mobilnisite/slovnik/gtp/) tunel s Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a slouží jako ukotvovací bod pro mobilitu, čímž zajišťuje stabilitu IP adresy uživatele při jeho pohybu. V 5G Core (5GC) je tato funkce distribuována napříč UPF, která poskytuje ukotvovací bod [PDU](/mobilnisite/slovnik/pdu/) relace. DT provádí hlubokou inspekci paketů, detekci aplikací a může interagovat s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a účtovací funkcí ([CHF](/mobilnisite/slovnik/chf/)) za účelem aplikace politik specifických pro službu a zaznamenávání využití.

Jak to funguje, zahrnuje několik klíčových procesů. Když UE zahájí PDU relaci, síť vybere bod DT (např. UPF). DT přidělí UE IP adresu, nastaví potřebné přeposílací pravidla a vytvoří tunel N3 (nebo N9) směrem k přístupové síti. Všechny pakety uživatelské roviny z UE procházejí tímto bodem DT, který je následně směruje dál na základě cílových IP adres a síťových politik. Pro downlinkový provoz určený pro UE přijímá DT pakety z externí sítě, zapouzdřuje je do příslušného tunelu a přeposílá je ke správné základnové stanici. Průběžně spravuje relaci, aplikuje QoS značkování, generuje účtovací záznamy a může iniciovat procedury modifikace relace na základě pokynů sítě.

## K čemu slouží

Funkce Data Termination existuje za účelem poskytnutí stabilní, řízené a politikami kontrolované brány mezi zařízením mobilního uživatele a širokou škálou externích paketových datových sítí. Řeší základní problém, jak připojit mobilní zařízení s podporou IP ke službám na internetu nebo privátních sítích, a přitom zachovat kontrolu operátora nad spojením. Před existencí takových ukotvovacích bodů rané datové služby postrádaly konzistentní podporu mobility, sofistikované účtování a schopnost aplikovat dynamické politiky na základě typu předplatného uživatele nebo aplikace.

Vytvoření a formalizace konceptu DT v architekturách 3GPP (GPRS, EPC, 5GC) bylo motivováno potřebou škálovatelných, bezpečných a účtovatelných mobilních datových služeb. Odstraňuje omezení jednoduchého IP směrování zavedením síťově řízeného ukončovacího bodu, který může ukotvit relaci uživatele, což umožňuje plynulé předávání mezi základnovými stanicemi bez přerušení probíhajících TCP/IP spojení. To je klíčové pro zážitek neustálého připojení, který uživatelé očekávají. DT navíc umožňuje nadstandardní služby, jako jsou vyhrazené přenosové kanály pro IMS hlas, tvarování provozu nebo rodičovské kontroly, protože je právě tím místem, kde se vynucují politiky operátora.

Historicky, jak se buněčné sítě vyvíjely z okruhově přepínané hlasové služby na paketově přepínaná data, se funkce DT stala základním kamenem architektury datové roviny. Poskytuje nezbytnou inteligenci v uživatelské rovině pro podporu komerčních datových služeb, včetně předplaceného účtování, diferenciace služeb a zákonného odposlechu. Její účel přesahuje pouhé zajištění konektivity; je hybatelem pro monetizaci a správu datového potrubí, zajišťuje efektivní využití síťových zdrojů v souladu s obchodními pravidly a regulatorními požadavky.

## Klíčové vlastnosti

- Ukotvuje PDU relaci nebo PDP kontext uživatele, čímž zajišťuje stabilitu IP adresy během mobility
- Rozhraní s externími paketovými datovými sítěmi (např. Internet, IMS)
- Vynucuje politiky a účtovací pravidla (rozhodnutí PCRF/PCF) na provoz v uživatelské rovině
- Generuje záznamy o využití pro offline a online účtovací systémy
- Provádí směrování a přeposílání provozu, včetně klasifikace uplink/downlink
- Může podporovat hlubokou inspekci paketů a detekci aplikací pro zpracování s ohledem na službu

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 23.919** (Rel-19) — 3GPP Direct Tunnel Deployment Guidelines
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TR 28.915** (Rel-19) — Management and orchestration; Study on Network Digital Twin
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [DT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dt/)
