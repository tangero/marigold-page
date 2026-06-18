---
slug: "baic"
url: "/mobilnisite/slovnik/baic/"
type: "slovnik"
title: "BAIC – Barring of All Incoming Calls"
date: 2025-01-01
abbr: "BAIC"
fullName: "Barring of All Incoming Calls"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/baic/"
summary: "BAIC je doplňková služba, která umožňuje mobilnímu účastníkovi zakázat všechny příchozí hovory. Poskytuje uživatelům kontrolu nad příjmem hovorů, což jim umožňuje vyhnout se rušení a spravovat své sou"
---

BAIC je doplňková služba, která umožňuje mobilnímu účastníkovi zakázat všechny příchozí hovory za účelem správy soukromí a vyhnutí se rušení.

## Popis

Barring of All Incoming Calls (BAIC, tedy Zákaz všech příchozích hovorů) je doplňková služba standardizovaná 3GPP, která oprávňuje obsluhovaného mobilního účastníka zabránit síti v dokončení jakéhokoli příchozího hovoru na jeho linku. Funguje jako služba založená na předplatném, kterou spravuje síťový operátor a která je konfigurována v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Je-li BAIC aktivní, síť při sestavování hovoru k účastníkovi provede kontrolu; pokud je služba aktivována, hovor je zakázán a volající strana obvykle obdrží hlášení nebo tón signalizující nedostupnost. Logika služby je prováděna v jádrové síti, konkrétně v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo v uzlech IP Multimedia Subsystem (IMS) pro okruhově spínanou a paketově spínanou doménu.

Z architektonického hlediska BAIC interaguje s procedurami řízení hovorů. Při pokusu o příchozí hovor Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje HLR/HSS na směrovací informace a stav účastníka. HLR/HSS vrací profil účastníka, který obsahuje i údaje o předplatném BAIC. Je-li BAIC aktivní, GMSC nebo obsluhující MSC nepokračuje v sestavení hovoru k obsluhujícímu uzlu účastníka. Místo toho spustí příčinu uvolnění a může připojit volajícího k příslušnému hlášení. Služba je ve výchozím stavu deaktivována a musí být účastníkem explicitně aktivována, obvykle pomocí kódů Unstructured Supplementary Service Data ([USSD](/mobilnisite/slovnik/ussd/)), interaktivního hlasového systému nebo rozhraní zákaznické podpory.

Mezi klíčové součásti zapojené do služby patří HLR/HSS, které ukládají servisní profil účastníka, MSC/MSC Server, který provádí logiku zákazu, a GMSC, který řeší směrování příchozích hovorů. BAIC je součástí rodiny doplňkových služeb zákazu hovorů, která zahrnuje také Barring of Outgoing Calls ([BAOC](/mobilnisite/slovnik/baoc/)), Barring of Outgoing International Calls ([BOIC](/mobilnisite/slovnik/boic/)) a Barring of Incoming Calls when roaming (BIC-Roam). Její implementace zajišťuje, že žádný příchozí hovor, bez ohledu na původ (národní, mezinárodní nebo od konkrétních čísel), nedosáhne k mobilní stanici účastníka, když je služba aktivní. Tím poskytuje definitivní stav 'nerušit' na úrovni sítě.

V kontextu moderních sítí se principy BAIC rozšiřují do služeb založených na IMS, kde lze podobný zákaz hovorů uplatnit na hovory Voice over LTE (VoLTE) prostřednictvím Initial Filter Criteria (iFC) ve Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)). Služba je klíčová pro soukromí a kontrolu uživatele a tvoří základní telekomunikační funkci. Její vynucování na síťové úrovni zajišťuje spolehlivost, neboť nezávisí na stavu nebo nastavení mobilního zařízení, a nabízí tak robustní mechanismus, jak mohou účastníci spravovat svou dostupnost.

## K čemu slouží

BAIC byl vytvořen, aby uspokojil potřebu účastníků mít absolutní kontrolu nad příjmem příchozích hovorů, a poskytuje spolehlivou metodu, jak se vyhnout nechtěnému rušení a zajistit soukromí. Před zavedením takových standardizovaných doplňkových služeb uživatelé spoléhali na řešení na úrovni zařízení, jako je vypnutí telefonu nebo zapnutí tichého režimu, která nebyla neprůstřelná a mohla vést k promeškání důležitých hovorů, pokud na ně uživatelé zapomněli. BAIC nabízí bariéru vynucovanou sítí, která zajišťuje, že při aktivaci nemohou žádné hovory proniknout, což je zásadní pro situace vyžadující zaručený nepřerušovaný čas, jako jsou schůzky, spánek nebo osobní krize.

Historicky, jak se mobilní telefonie koncem 90. a počátkem 2000. let stala všudypřítomnou, rostla poptávka po pokročilých funkcích řízených uživatelem. 3GPP zavedlo sadu doplňkových služeb ve verzi 5, včetně BAIC, aby tyto schopnosti standardizovalo napříč operátory a regiony a zajistilo interoperabilitu a konzistentní uživatelský zážitek. BAIC vyřešil omezení dřívějších základních hovorových služeb, kterým chyběla podrobná správa příchozích hovorů. Služba také doplňuje další služby zákazu hovorů a umožňuje účastníkům přizpůsobit svou dostupnost podle konkrétních potřeb, například zakázat pouze mezinárodní hovory nebo zakázat všechny hovory při roamingu.

Služba je motivována zejména požadavkem na soukromí a uživatelskou autonomii v telekomunikacích. Posiluje postavení účastníků bez závislosti na funkčnosti nebo stavu baterie mobilního zařízení, protože zákaz je prováděn v rámci síťové infrastruktury. Tento síťově orientovaný přístup zajišťuje, že služba funguje, i když je mobilní telefon zapnutý a registrovaný, a poskytuje tak silnější záruku než režimy 'nerušit' závislé na zařízení. BAIC tedy představuje základní telekomunikační službu, která vyvažuje konektivitu s uživatelem řízeným odpojením.

## Klíčové vlastnosti

- Zákaz všech příchozích hovorů k účastníkovi vynucovaný sítí
- Služba založená na předplatném spravovaná operátorem v HLR/HSS
- Aktivace a deaktivace pomocí USSD kódů nebo rozhraní operátora
- Integrace s procedurami řízení hovorů v jádrové síti v MSC/GMSC
- Poskytuje spolehlivý stav 'nerušit' nezávislý na nastavení zařízení
- Součást standardizované rodiny doplňkových služeb zákazu hovorů 3GPP

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [BAOC – Barring of All Outgoing Calls](/mobilnisite/slovnik/baoc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking

---

📖 **Anglický originál a plná specifikace:** [BAIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/baic/)
