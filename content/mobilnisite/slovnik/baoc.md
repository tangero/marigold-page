---
slug: "baoc"
url: "/mobilnisite/slovnik/baoc/"
type: "slovnik"
title: "BAOC – Barring of All Outgoing Calls"
date: 2025-01-01
abbr: "BAOC"
fullName: "Barring of All Outgoing Calls"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/baoc/"
summary: "BAOC je doplňková služba v sítích 3GPP, která účastníkovi umožňuje zablokovat veškeré odchozí hovory ze svého mobilního zařízení. Jde o službu řízenou uživatelem, která brání zahájení hlasových hovorů"
---

BAOC je doplňková služba v sítích 3GPP, která účastníkovi umožňuje zablokovat veškeré odchozí hovory ze svého mobilního zařízení.

## Popis

Barring of All Outgoing Calls (BAOC) je standardizovaná doplňková služba definovaná v rámci specifikací 3GPP pro okruhově spínané telefonní služby. Funguje jako součást funkcí řízení hovorů spravovaných jádrem sítě, konkrétně v interakci s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v sítích GSM/UMTS nebo s MSC Server v sítích založených na IMS pro scénáře navázání na legacy okruhově spínané služby. Služba je vyvolána během fáze sestavování hovoru; když se účastník s aktivní službou BAOC pokusí zahájit hlasový hovor, MSC zachytí žádost o sestavení hovoru, zkontroluje profil služeb účastníka a použije logiku blokování, což vede k zamítnutí hovoru ještě před přidělením jakýchkoli rádiových prostředků pro odchozí část.

Architektura pro BAOC spoléhá na Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) jako centrální úložiště dat služeb účastníka. HLR ukládá informace o předplatném BAOC jako součást profilu účastníka a přenáší tato data do obsluhujícího MSC/[VLR](/mobilnisite/slovnik/vlr/) (Visitor Location Register), když se účastník registruje v síti. K tomuto přenosu dochází prostřednictvím protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)), konkrétně pomocí operace Insert Subscriber Data. MSC/VLR poté tato data uchovává lokálně pro rychlý přístup během zpracování hovoru. Službu lze typicky aktivovat, deaktivovat nebo dotazovat pomocí standardizovaných kódů Unstructured Supplementary Service Data ([USSD](/mobilnisite/slovnik/ussd/)) nebo v pozdějších vydáních prostřednictvím řídicích mechanismů služeb IP Multimedia Subsystem (IMS).

Z procedurálního hlediska provádí kontrolu blokování funkce Call Control v MSC. Po přijetí žádosti o zahájení hovoru (např. [CM](/mobilnisite/slovnik/cm/)_SERVICE_REQUEST) se MSC dotazuje svého lokálního záznamu VLR pro daného účastníka. Je-li indikátor BAOC aktivní, MSC vygeneruje zpět k mobilní stanici zamítavou zprávu řízení hovoru, často s konkrétním kódem příčiny označujícím 'odchozí hovory blokovány'. Služba se liší od blokování iniciovaného operátorem a je určena pro řízení účastníkem. Její implementace je úzce integrována s dalšími doplňkovými službami, jako je Barring of Outgoing International Calls ([BOIC](/mobilnisite/slovnik/boic/)) a Barring of Outgoing International Calls except those directed to the Home [PLMN](/mobilnisite/slovnik/plmn/) Country (BOIC-exHC), a vytváří tak hierarchii možností blokování.

Ve vývoji směrem k plně IP sítím jsou principy BAOC zachovány pro tísňová volání a další nezbytné služby. Je důležité poznamenat, že BAOC nesmí blokovat tísňová volání (na čísla jako 112 nebo 911), jak to vyžadují regulatorní požadavky. Logika řízení hovorů v síti zahrnuje kontrolu výjimky pro tísňová čísla před aplikací omezení BAOC. V systémech 5G, kde je nativní hlas přenášen přes IMS (VoNR), nejsou tradiční okruhově spínané doplňkové služby jako BAOC přímo definovány. Ekvivalentní řízení služeb pro odchozí hlasové relace je však zajištěno aplikačními servery IMS a řízením politik, což zajišťuje kontinuitu funkcí blokování hovorů řízených uživatelem v paketově spínané doméně.

## K čemu slouží

BAOC byla vytvořena, aby poskytla mobilním účastníkům přímou kontrolu nad jejich možností uskutečňovat odchozí hlasové hovory a řešila tak potřeby správy nákladů, rodičovské kontroly a omezení používání zařízení. V rané éře GSM vytvořily fakturační modely postpaid, a zejména prepaid, poptávku po nástrojích k zabránění neočekávaných poplatků za odchozí hovory. Účastník mohl aktivovat BAOC, aby se vyhnul uskutečňování hovorů, například při půjčování telefonu dítěti nebo pro kontrolu využití firemního zařízení. Tato kontrola iniciovaná účastníkem ji odlišovala od blokovacích služeb síťového operátora používaných z administrativních důvodů, jako je správa dluhů.

Služba řešila omezení spočívající v tom, že možnosti blokování existovaly pouze na straně operátora. Před standardizací těchto doplňkových služeb musela být jakákoli omezení hovorů aplikována síťovým operátorem na HLR ručně, což bylo neefektivní pro dočasné potřeby řízené uživatelem. BAOC jako součást portfolia doplňkových služeb GSM Phase 2+ posílila postavení uživatele. Její vytvoření bylo motivováno širším cílem 3GPP poskytnout funkční paritu a nadřazenost vůči digitálním pevným sítím (ISDN), které nabízely podobné doplňkové služby blokování hovorů. Stala se základním prvkem souboru možností blokování hovorů, což uživatelům poskytlo detailní kontrolu.

BAOC dále zavedla standardizovanou, na síť orientovanou implementaci, která zajišťovala spolehlivost a interoperabilitu napříč různými síťovými dodavateli a operátory. Zpracování blokování v MSC jádra sítě poskytovalo ve srovnání s potenciálními řešeními na straně klienta v mobilním zařízení bezpečnou a proti zásahům odolnou metodu. Návrh služby také z podstaty respektoval regulatorní požadavky tím, že zajišťoval přístup k tísňovým hovorům, a vyvažoval tak uživatelskou kontrolu s nezbytnými bezpečnostními nařízeními. Její dlouhověkost napříč vydáními 3GPP zdůrazňuje její užitečnost jako základní, ale vitální telekomunikační služby pro ochranu spotřebitele a řízenou mobilitu.

## Klíčové vlastnosti

- Aktivace a deaktivace řízená účastníkem prostřednictvím USSD nebo síťových menu
- Vynucování na síťové bázi v MSC/VLR při zahájení hovoru
- Ukládání dat o předplatném v HLR s propagací do VLR
- Explicitní výjimka pro uskutečnění tísňového volání (např. 112, 911)
- Integrace s protokolem MAP pro správu dat účastníka
- Součást doplňující sady služeb blokování odchozích hovorů (BOIC, BOIC-exHC)

## Související pojmy

- [BOIC – Barring of Outgoing International Calls](/mobilnisite/slovnik/boic/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking

---

📖 **Anglický originál a plná specifikace:** [BAOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/baoc/)
