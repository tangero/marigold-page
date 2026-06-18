---
slug: "vt-csi"
url: "/mobilnisite/slovnik/vt-csi/"
type: "slovnik"
title: "VT-CSI – Visited Terminating CAMEL Subscription Information"
date: 2025-01-01
abbr: "VT-CSI"
fullName: "Visited Terminating CAMEL Subscription Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vt-csi/"
summary: "VT-CSI je soubor dat CAMEL předplatného stažených z HLR účastníka do VLR navštívené sítě. Umožňuje provedení přizpůsobených, operátorem definovaných služeb Intelligent Network (IN) – jako je předplace"
---

VT-CSI je soubor dat CAMEL předplatného odeslaných do VLR navštívené sítě, aby umožnil domácí síti řízení služeb Intelligent Network, jako je předplacené účtování, pro příchozí hovory k roamujícímu účastníkovi.

## Popis

VT-CSI (Visited Terminating [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information) je kritická datová struktura v systému Customised Applications for Mobile networks Enhanced Logic (CAMEL). CAMEL je standard Intelligent Network ([IN](/mobilnisite/slovnik/in/)) pro sítě GSM, UMTS a LTE, který umožňuje síťovým operátorům definovat a nasazovat vlastní hodnotově přidané služby, které fungují konzistentně i při roamingu účastníka. VT-CSI se konkrétně týká služeb spouštěných událostmi typu mobile-terminating, jako je příchozí hlasový hovor, [SMS](/mobilnisite/slovnik/sms/) nebo paketová datová relace adresovaná účastníkovi.

Z architektonického hlediska je VT-CSI součástí profilu účastníka uloženého v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Když účastník přejde do roamingu v nové síťové oblasti, jeho profil, včetně případných dat VT-CSI, je přenesen do Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v navštívené síti jako součást procedury aktualizace polohy. VT-CSI obsahuje soubor triggerů a přidružených instrukcí. Tyto triggery jsou detekční body v rámci modelu hovoru v Visited Mobile Switching Center ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo uzlu navštívené sítě. Když dorazí příchozí hovor pro účastníka do VMSC a stavový automat zpracování hovoru narazí na detekční bod nakonfigurovaný v VT-CSI, CAMEL Service Switching Function (gsmSSF) v VMSC pozastaví zpracování hovoru a zahájí dialog s určenou CAMEL Service Control Function (gsmSCF) v domácí síti účastníka.

Jak to funguje, zahrnuje výměnu signalizace v reálném čase. Po detekci triggeru odešle gsmSSF v navštívené síti zprávu Initial Detection Point (IDP) do gsmSCF v domácí síti prostřednictvím protokolu CAMEL Application Part (CAP). Tato zpráva obsahuje podrobnosti o hovoru a účastníkovi. Domácí gsmSCF, který hostí servisní logiku (např. kontrolu předplaceného zůstatku), poté vyhodnotí požadavek a odešle zpět instrukce ve zprávě Connect nebo Continue. Tyto instrukce mohou přikázat navštívenému VMSC, aby hovor spojil, aplikoval specifické účtování, přehrál oznámení nebo dokonce přesměroval hovor na základě servisní logiky domácího operátora. To umožňuje domácímu operátorovi zachovat kontrolu nad tím, jak jsou služby aplikovány na jeho účastníky, bez ohledu na schopnosti navštívené sítě.

Klíčovými komponentami jsou HLR (úložiště dat), VLR/SGSN (dočasné úložiště dat v navštívené síti), VMSC/gsmSSF (detekce triggerů a komutace) a domácí gsmSCF (provedení servisní logiky). Jeho role spočívá v oddělení servisní logiky od základní komutační funkčnosti, což umožňuje rychlé nasazení komplexních služeb, jako je předplacený roaming, blokování příchozích hovorů, personalizované vyzváněcí tóny nebo kontrola podvodů pro terminující hovory. Zajišťuje, že uživatelský zážitek účastníka a obchodní pravidla operátora jsou konzistentně vynucována globálně.

## K čemu slouží

VT-CSI bylo vytvořeno, aby vyřešilo hlavní omezení raného mobilního roamingu: neschopnost operátora domácí sítě aplikovat své vlastní inteligentní služby na účastníky, když byli mimo jeho síť. Před CAMEL mohl roamující účastník ztratit přístup ke své domácí předplacené službě nebo vlastním funkcím pro obsluhu hovorů, protože navštívená síť neměla o těchto službách informace ani schopnost je provádět. To vytvářelo špatný uživatelský zážitek a omezovalo příležitosti operátorů k výnosům.

Vývoj standardu CAMEL a v něm VT-CSI byl motivován komerční potřebou konzistentního poskytování služeb. Řeší tento problém tím, že umožňuje domácí síti 'vložit' své triggery servisní logiky (CSI) do navštívené sítě. Pro terminující hovory to znamenalo, že domácí operátor mohl stále kontrolovat, jak je příchozí hovor obsluhován – například kontrolovat předplacený zůstatek před tím, než se hovor dovolá na telefon, i když veškerá komutace probíhala v cizí síti. To umožnilo úspěšné zavedení předplaceného roamingu, což byl obrovský hybatel trhu.

Historicky se vyvinulo z konceptů IN pro pevné linky, jako je INAP. Jeho vytvoření standardizovalo rozhraní (CAP) a datové struktury (jako CSI), takže jakákoli navštívená síť vyhovující 3GPP mohla interagovat s jakýmkoli servisním řídicím bodem domácí sítě. Tato interoperabilita byla zásadní pro globální nasazení služeb. VT-CSI se konkrétně zaměřuje na terminující větev, čímž doplňuje další typy CSI, jako je O-CSI (pro originating hovory), a dává operátorům komplexní kontrolu nad zážitkem jejich účastníků z hovorů po celém světě.

## Klíčové vlastnosti

- Uloženo v HLR a staženo do VLR/SGSN během registrace při roamingu
- Obsahuje triggery pro události řízení mobile-terminating hovorů v navštívené síti
- Umožňuje signalizaci v reálném čase (CAP) mezi navštíveným gsmSSF a domácím gsmSCF
- Umožňuje domácímu operátorovi řídit servisní logiku pro příchozí hovory k roamujícím účastníkům
- Nezbytné pro implementaci předplaceného účtování na terminujících hovorech při roamingu
- Podporuje vlastní služby jako filtrování hovorů, překlad čísel nebo informace o ceně hovoru

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [O-CSI – Originating CAMEL Subscription Information](/mobilnisite/slovnik/o-csi/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [VT-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/vt-csi/)
