---
slug: "sim-s"
url: "/mobilnisite/slovnik/sim-s/"
type: "slovnik"
title: "SIM-S – SEAL Identity Management Server"
date: 2025-01-01
abbr: "SIM-S"
fullName: "SEAL Identity Management Server"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sim-s/"
summary: "Síťová funkční komponenta, která v rámci architektury správy identit SEAL funguje jako server. Umožňuje vydávání, ověřování a správu decentralizovaných identit a ověřitelných přihlašovacích údajů pro"
---

SIM-S je SEAL Identity Management Server (server správy identit SEAL), síťová komponenta, která vydává, ověřuje a spravuje decentralizované identity a ověřitelné přihlašovací údaje (verifiable credentials) a slouží jako důvěryhodný bod (trust anchor) mezi vydavateli, držiteli a ověřovateli.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Identity Management Server (SIM-S) je funkční entita na straně serveru, specifikovaná v rámci architektury 3GPP SEAL pro enabler správy identit. Typicky je nasazena v doméně síťového operátora nebo důvěryhodné třetí strany na edge nebo v cloudu. SIM-S poskytuje služby správy identit SEAL Identity Management klientům ([SIM-C](/mobilnisite/slovnik/sim-c/)) a dalším SEAL enablerům. Jejím hlavním úkolem je podpora operací souvisejících s decentralizovanými identifikátory (DID) a ověřitelnými přihlašovacími údaji ([VC](/mobilnisite/slovnik/vc/)) podle definic [W3C](/mobilnisite/slovnik/w3c/), přizpůsobených v rámci 3GPP.

Architektonicky může SIM-S plnit několik rolí z modelu VC, například Verifiable Data Registry (důvěryhodný systém pro zaznamenávání DID a s nimi spojených veřejných klíčů), DID Resolver (služba, která získává DID dokumenty z registru) nebo důvěryhodný zprostředkovatel mezi vydavateli a držiteli. Vystavuje northbound a southbound [API](/mobilnisite/slovnik/api/). Na jih (southbound) komunikuje s SIM-C pomocí RESTful API přes zabezpečené kanály (např. [TLS](/mobilnisite/slovnik/tls/) s vzájemným ověřováním). Na sever (northbound) může rozhraním komunikovat s vydavateli přihlašovacích údajů (např. backendem operátora, který vydává přihlašovací údaje k předplaceným službám), dalšími instancemi SIM-S nebo ověřovateli (edge aplikačními servery). SIM-S spravuje potřebné důvěryhodné body (trust anchors), jako jsou veřejné klíče důvěryhodných vydavatelů nebo kořenové certifikáty pro DID metody.

Princip fungování spočívá v zprostředkování klíčových událostí životního cyklu identity. Při vydání může vydavatel (např. mobilní operátor) instruovat SIM-S, aby vytvořil DID a vydal odpovídající ověřitelný přihlašovací údaj pro účastníka/zařízení. SIM-S může spravovat DID v registru a poté doručit přihlašovací údaj SIM-C účastníka. Při ověřování, když edge služba (ověřovatel) potřebuje zkontrolovat přihlašovací údaj předložený SIM-C, může dotazovat SIM-S, aby rozřešil příslušný DID, získal veřejné klíče vydavatele nebo ověřil stav přihlašovacího údaje (např. zkontroloval zneplatnění). SIM-S tyto kontroly provádí na základě nakonfigurovaných vztahů důvěry a vrací výsledek ověření. Tím odlehčuje lehkým edge ověřovatelům od složité správy důvěry a kryptografické verifikační logiky a poskytuje centralizovaný bod pro vynucování politik identity v rámci ekosystému SEAL. Umožňuje škálovatelnou a interoperabilní důvěru napříč různými administrativními doménami v edge computingu.

## K čemu slouží

SIM-S byl vytvořen, aby poskytl standardizovanou, síťově hostovanou autoritu pro správu moderních decentralizovaných identit v rámci architektury 5G service enabler. S rozšiřováním edge computingu služby potřebují způsob, jak rychle a lokálně ověřovat atributy uživatele/zařízení bez neustálého odkazování na centrální core síť. Tradiční autentizace založená na [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/) není navržena pro podrobné, atributové ověřování pro aplikace třetích stran na edge.

Řeší problém zprostředkování důvěry v fragmentovaném edge prostředí. Bez SIM-S by si musel každý poskytovatel edge aplikací vytvářet přímé vztahy důvěry s každým potenciálním vydavatelem identity (např. s každým mobilním operátorem), což je nepraktické. SIM-S funguje jako důvěryhodný zprostředkovatel, na kterého se aplikace mohou dotazovat. Pro operátory poskytuje řízený způsob, jak rozšířit důvěru mobilního předplatného do edge domény vydáváním a správou ověřitelných přihlašovacích údajů odvozených z tohoto předplatného.

Motivace vychází z potřeby umožnit bezpečný a soukromí respektující přístup ke službám pro nové 5G vertikály. Adopcí standardních modelů W3C pro ověřitelné přihlašovací údaje SIM-S usnadňuje interoperabilitu s širšími ekosystémy digitální identity mimo telekomunikace. Umožňuje uživatelům prokazovat konkrétní tvrzení (např. "věk nad 18 let", "má prémiové předplatné") edge službám bez odhalení plné identity (IMSI/SUPI), čímž podporuje principy privacy-by-design. Jeho vytvoření formalizuje roli operátora jako poskytovatele identity v hodnotovém řetězci edge computingu, otevírá nové zdroje příjmů a zvyšuje bezpečnost služeb.

## Klíčové vlastnosti

- Implementace protokolů správy identit SEAL pro decentralizovanou identitu na straně serveru
- Funguje jako Verifiable Data Registry a/nebo DID Resolver pro správu decentralizovaných identifikátorů (DID)
- Umožňuje vydávání, zneplatnění a kontrolu stavu ověřitelných přihlašovacích údajů (Verifiable Credentials)
- Poskytuje služby ověřování přihlašovacích údajů edge aplikačním serverům (ověřovatelům)
- Spravuje důvěryhodné body (trust anchors) a politiky pro vydavatele identit v rámci ekosystému SEAL
- Vystavuje standardizovaná northbound a southbound RESTful API pro interoperabilitu

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [SIM-C – SEAL Identity Management Client](/mobilnisite/slovnik/sim-c/)

## Definující specifikace

- **TS 24.547** (Rel-19) — SEAL Identity Management Protocol
- **TS 33.434** (Rel-19) — Security aspects of SEAL for verticals

---

📖 **Anglický originál a plná specifikace:** [SIM-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/sim-s/)
