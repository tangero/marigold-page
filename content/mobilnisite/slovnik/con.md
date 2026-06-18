---
slug: "con"
url: "/mobilnisite/slovnik/con/"
type: "slovnik"
title: "CON – CONference calling"
date: 2025-01-01
abbr: "CON"
fullName: "CONference calling"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/con/"
summary: "CON je doplňková služba v sítích 3GPP umožňující více účastníkům připojit se k jednomu hlasovému hovoru. Umožňuje uživateli zřídit konferenční hovor pozváním dalších stran a podporuje jak ad-hoc, tak"
---

CON je doplňková služba v sítích 3GPP, která umožňuje uživateli zřídit hlasové hovory s více účastníky (konferenční hovor) prostřednictvím pozvání dalších účastníků a podporuje jak ad-hoc, tak předem připravené konference.

## Popis

CON (CONference calling, konferenční hovor) je standardizovaná doplňková služba definovaná ve specifikacích 3GPP, která umožňuje hlasovou komunikaci více účastníků v rámci mobilních sítí. Funguje jako služba na aplikační vrstvě řízená jádrem sítě, konkrétně v rámci IP Multimedia Subsystem (IMS) pro paketově přepínané domény a v obvodu přepínaném jádru pro starší sítě. Služba umožňuje uživateli, známému jako kontrolér nebo iniciátor konference, zřídit konferenční hovor postupným nebo současným přidáním dalších účastníků, kteří mohou být mobilní účastníci nebo uživatelé pevných linek. Konference může být ad-hoc, vytvořená dynamicky během hovoru, nebo předem připravená s naplánovaným časem začátku a seznamem účastníků. Mezi klíčové síťové prvky zapojené do služby patří Serving Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v IMS, která zajišťuje řízení relace, a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která poskytuje schopnost míchání médií pro spojení audio streamů od všech účastníků do jednoho soudržného výstupu pro každého účastníka.

Architektura CON se opírá o signalizační protokoly jako [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) v implementacích založených na IMS a [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) v obvodu přepínaných scénářích. Když uživatel zahájí konferenci, síť přidělí konferenční prostředky, včetně konferenčního můstku v MRF, který míchá pakety zvuku v reálném čase. Účastníci jsou připojeni přes přenosové cesty, které přenášejí hlasová data, přičemž MRF zajišťuje synchronizaci a spravuje identifikaci mluvčího, potlačení ozvěn a vyrovnávání hlasitosti. Služba podporuje různé stavy konference, jako je aktivní, pozastavená nebo ukončená, a umožňuje kontrolérovi spravovat hovor přidáváním, odebíráním nebo izolováním účastníků. V IMS je CON integrována s dalšími doplňkovými službami, jako je hold (přidržení hovoru) a call transfer (přesměrování hovoru), což umožňuje plynulou interakci uživatelů prostřednictvím správy založené na rozhraní Ut nebo signalizace během hovoru.

Implementace CON zahrnuje funkce jako uzamčení konference pro zabránění neoprávněnému přidávání, subkonference pro soukromé vedlejší rozhovory a rozdílné účtování pro iniciátory oproti účastníkům. Služba je definována v mnoha specifikacích 3GPP, včetně TS 23.279 pro architekturu, TS 24.508 pro signalizační procedury, TS 29.235 pro řízení médií a TS 32.808 pro aspekty účtování. Podporuje interoperabilitu se sítěmi mimo 3GPP prostřednictvím bran, což zajišťuje, že se konferenčních hovorů mohou účastnit i účastníci z [PSTN](/mobilnisite/slovnik/pstn/) nebo jiných VoIP systémů. Robustnost služby je zvýšena mechanismy pro zpracování chyb, jako je návrat k bilaterálnímu hovoru, pokud nejsou k dispozici konferenční prostředky, a prioritizací kvality služby (QoS) pro zachování nízké latence a vysoké kvality zvuku během hovorů s více účastníky.

## K čemu slouží

CON byla zavedena, aby řešila rostoucí potřebu efektivní skupinové komunikace v mobilních sítích, zejména pro podnikovou spolupráci, rodinné diskuze a koordinaci v nouzových situacích. Před její standardizací bylo hovorů s více účastníky často možné dosáhnout pouze pomocí proprietárních řešení nebo bylo nutné použít externí konferenční můstky, což vedlo k problémům s interoperabilitou a nekonzistentním uživatelským zážitkům. Definování CON jako doplňkové služby ve 3GPP Release 7 poskytlo jednotnou, síťově nativní schopnost, která mohla být plynule integrována do stávajících mobilních infrastruktur, což snížilo závislost na službách třetích stran a zvýšilo spolehlivost služby.

Vytvoření CON bylo motivováno expanzí mobilní telefonie do profesionálního prostředí, kde se konferenční hovory staly nezbytnými pro vzdálená jednání a rozhodování. Vyřešila omezení starších ad-hoc metod, jako je call waiting (čekání na hovor) a ruční spojování hovorů, které byly těžkopádné a postrádaly funkce jako správa účastníků nebo centralizované míchání médií. Standardizace CON zajistila konzistentní chování napříč operátory a zařízeními, podporovala jak obvodově přepínané, tak paketově přepínané domény a později se vyvinula, aby byla v souladu s architekturami IMS pro sítě typu all-IP. To umožnilo operátorům nabízet služby s přidanou hodnotou, generovat dodatečné příjmy z poplatků za konferenční hovory a zlepšit spokojenost uživatelů tím, že umožnila intuitivní interakce s více účastníky přímo z mobilních přístrojů.

## Klíčové vlastnosti

- Zřízení hlasové relace s více účastníky až do několika účastníků
- Podpora ad-hoc a předem připravených typů konferencí
- Schopnosti kontroléra konference pro přidávání, odebírání a izolování účastníků
- Integrace s mediálními prostředky IMS prostřednictvím MRF pro míchání zvuku
- Spolupráce s obvodově přepínanými a paketově přepínanými sítěmi
- Rozdílné účtování pro iniciátora a účastníky

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [CON na 3GPP Explorer](https://3gpp-explorer.com/glossary/con/)
