---
slug: "o-ue"
url: "/mobilnisite/slovnik/o-ue/"
type: "slovnik"
title: "O-UE – Originating User Equipment"
date: 2025-01-01
abbr: "O-UE"
fullName: "Originating User Equipment"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/o-ue/"
summary: "Uživatelské zařízení (UE), které zahajuje komunikační relaci, například hlasový hovor, videohovor nebo datovou relaci. V kontextu směrování hovorů a servisní logiky jde o zařízení volající strany. Jeh"
---

O-UE je uživatelské zařízení (User Equipment), které zahajuje komunikační relaci, vystupuje jako zařízení volající strany a spouští síťové procedury pro iniciátora.

## Popis

Originating User Equipment (O-UE) je logická role přiřazená mobilnímu zařízení (například telefonu nebo datovému terminálu) v okamžiku, kdy iniciuje požadavek na navázání komunikační relace. Jde o základní koncept v komunikačních modelech a servisní architektuře 3GPP, platný napříč službami s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), přepojováním paketů ([PS](/mobilnisite/slovnik/ps/)) a službami založenými na IMS. O-UE je koncový bod, který vysílá [SIP](/mobilnisite/slovnik/sip/) INVITE pro IMS hlasový hovor, zasílá zprávu SETUP pro CS hovor nebo aktivuje kontext Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) pro datovou relaci. Síť identifikuje zařízení jako O-UE na základě směru požadavku na navázání relace.

Když O-UE odešle počáteční servisní požadavek, spustí kaskádu síťových procedur. V řídicí rovině je požadavek směrován na příslušný řídicí uzel jádra sítě – na [MSC](/mobilnisite/slovnik/msc/) Server pro CS hovory, na [MME](/mobilnisite/slovnik/mme/) pro připojení v LTE nebo na [S-CSCF](/mobilnisite/slovnik/s-cscf/) pro IMS relace. Tento uzel následně autentizuje účastníka pomocí přihlašovacích údajů uložených na modulu [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) v UE. Síť zkontroluje servisní profil účastníka v HSS, aby zjistila, jaké služby jsou povoleny (např. může tento uživatel uskutečnit mezinárodní hovory?). Pro účtování síť začne generovat záznamy o účtování spojené s identitou O-UE (např. MSISDN).

Role O-UE je klíčová pro provedení servisní logiky pro iniciátora. V architekturách Inteligentní sítě (IN), jako je CAMEL, je na síťovém uzlu obsluhujícím O-UE spuštěn detekční bod (Detection Point, DP) pro 'Collected_Info' nebo 'Analysed_Information'. To umožňuje řídicímu bodu služeb (Service Control Point, SCP) domovské sítě aplikovat vlastní logiku, jako je kontrola předplaceného kreditu nebo transformace čísla, ještě před dalším směrováním hovoru. V IMS aplikuje S-CSCF na straně iniciátora počáteční filtrační kritéria (initial Filter Criteria, iFC) pro spuštění aplikačních serverů poskytujících služby, jako je filtrování hovorů nebo hlasová schránka. Fyzická a protokolová vrstva O-UE je shodná s jakýmkoli jiným UE; jeho označení je čistě situační v rámci konkrétního dialogu nebo transakce.

## K čemu slouží

Termín O-UE existuje, aby poskytoval jasný a konzistentní referenční bod ve specifikacích 3GPP pro všechny procedury a servisní logiku, které závisí na tom, která strana relaci zahájila. V telekomunikacích podléhají volající a volaná strana různým regulacím, modelům účtování a zacházení se službami. Formální definice role O-UE zajišťuje, že chování sítě je v normách 3GPP jednoznačné. Například legální odposlech vyžaduje zachycení odlišných dat pro iniciátora oproti příjemci. Podobně systémy účtování musí uplatňovat tarify na účet O-UE, nikoli na účet koncového UE (Terminating UE).

Historicky byl tento rozdíl v telefonii implicitní, ale v digitálních mobilních sítích byl explicitně modelován, aby podpořil pokročilé funkce. Jak se sítě vyvíjely od základního hlasu k podpoře předplacených služeb, přenositelnosti čísel a složitých pravidel přesměrování hovorů, stala se potřeba ukotvit logiku k iniciátorovi prvořadá. Koncept O-UE umožňuje síti izolovat a zpracovávat 'iniciační větev' hovoru nezávisle. To je obzvláště důležité v roamingu, kde je O-UE obsluhováno navštívenou sítí, ale jeho servisní profil sídlí v domovské síti. Navštívená síť musí zařízení rozpoznat jako O-UE, aby mohla správně komunikovat s domovskou sítí pro řízení kreditu a autorizaci služeb, a zajistila tak konzistentní uživatelský zážitek bez ohledu na polohu.

## Klíčové vlastnosti

- Definuje UE, které iniciuje požadavek na navázání relace (hovor, datová relace, IMS dialog)
- Spouští v síti procedury autentizace, autorizace a účtování (AAA) pro iniciátora
- Určuje uplatnění řídicích pravidel pro hovory/služby na straně iniciátora (např. blokování, kontroly předplaceného kreditu)
- Jeho identita (např. IMSI, MSISDN) je použita jako účtovaná strana za relaci
- Ukotvuje provedení servisní logiky pro iniciátora v CAMEL nebo na IMS aplikačních serverech
- Jde o logickou roli; jakékoli UE se může stát O-UE, když zahájí komunikaci

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [T-UE – Terminating User Equipment](/mobilnisite/slovnik/t-ue/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)

---

📖 **Anglický originál a plná specifikace:** [O-UE na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-ue/)
