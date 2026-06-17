---
slug: "chv"
url: "/mobilnisite/slovnik/chv/"
type: "slovnik"
title: "CHV – Card Holder Verification"
date: 2025-01-01
abbr: "CHV"
fullName: "Card Holder Verification"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/chv/"
summary: "Card Holder Verification (CHV) je bezpečnostní mechanismus ve specifikacích 3GPP pro ověření uživatele UICC nebo SIM karty. Chrání přístup ke službám a datům karty vyžadováním PINu, což zajišťuje, že"
---

CHV je bezpečnostní mechanismus ve specifikacích 3GPP, který ověřuje uživatele UICC nebo SIM karty vyžadováním PINu, aby chránil služby a data karty proti neautorizovanému přístupu.

## Popis

Card Holder Verification (CHV) je bezpečnostní funkce definovaná ve specifikacích 3GPP, primárně pro Universal Integrated Circuit Cards (UICC) a Subscriber Identity Modules (SIM). Jejím hlavním účelem je ověřit osobu, která se pokouší kartu používat, a tím chránit citlivá data účastníka, přístupové údaje do síťě a uložené aplikace. Mechanismus CHV funguje tak, že vyžaduje od uživatele předložení tajného kódu, typicky Personal Identification Number (PIN), který je ověřen kartou samotnou před poskytnutím přístupu k chráněným funkcím. Toto ověření je lokální proces mezi uživatelským zařízením (např. mobilním telefonem) a kartou, který nezasahuje síť, což ho činí klíčovou první linii obrany proti zneužití zařízení a služeb.

Architektura CHV je integrována do bezpečnostní architektury UICC. Karta obsahuje CHV soubor ([EF](/mobilnisite/slovnik/ef/)_CHV), který uchovává referenční hodnotu PINu a stavové informace (např. povolen/blokován, počet zbývajících pokusů ověření). Když uživatel zadá PIN prostřednictvím rozhraní zařízení, zařízení zasílá příkaz VERIFY (dle [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-4) do UICC, předkládající zadánou hodnotu. Operační systém UICC porovná tuto předloženou hodnotu s uloženou referenční. Pokud se shodují, ověření je úspěšné a karta poskytne odpovídající úroveň přístupu. Pokud ověření selže, pokusový čítač se sníží. Po nastavitelném počtu po sobě jdoucích neúspěšných pokusů (typicky tři nebo více) se CHV zablokuje a vyžaduje PUK (PIN Unblocking Key) k jeho resetování, což zabraňuje útoku hrubou silou.

CHV řídí přístup ke kritickým souborům a funkcím na kartě. Primární CHV, často nazývaný CHV1 nebo PIN, typicky chrání přístup ke telefonnímu seznamu (EF_[ADN](/mobilnisite/slovnik/adn/)) a jiným souborům uživatelských dat. Druhý CHV (CHV2 nebo ADM1) může být definován pro ochranu administrativních funkcí. Role tohoto mechanismu je základní; zajišťuje, že samotné fyzické držení SIM karty není dostatečné pro přístup do mobilní síťě nebo k osobním datům. Funguje spolu s dalšími bezpečnostními vrstvami, jako je protokol Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) pro síťové ověření, vytvářející vícevrstvý bezpečnostní model, kde CHV poskytuje ověření uživatele a AKA poskytuje dvoustranné ověření mezi síťou a kartou.

Z procedurálního pohledu správa CHV zahrnuje povolení, zakázání, změnu a odblokování PINu. Tyto operace jsou prováděny prostřednictvím specifických příkazů z terminálu do UICC. Specifikace 3GPP, konkrétně TS 31.101 (UICC-Terminal Interface) a specifikace USIM aplikace (TS 31.102), detailně popisují přesné sekvence příkazů-odpovědí a struktury souborů. Mechanismus CHV je standardizovaná implementace ověření tajného kódu typu challenge-response, která zajišťuje interoperabilitu mezi různými výrobci karet a mobilních zařízení při zachování konzistentního bezpečnostního základu pro moduly identifikace účastníka.

## K čemu slouží

CHV byl vytvořen k řešení kritické potřeby ověření uživatele na úrovni zařízení v mobilních telekomunikacích. Rané mobilní systémy neměly robustní osobní bezpečnostní funkce pro SIM kartu samotnou. Pokud zařízení bylo ztraceno nebo ukradeno, každý mohlo vložit SIM do jiného telefonu a získat přístup do síťě, potenciálně způsobující náklady nebo zosobňující účastníka. Primární problém, který CHV řeší, je oddělení vlastnictví zařízení od autorizace služby; zajišťuje, že legitimní účastník se musí ověřit, aby mohlo využívat službu, i na svém vlastním nebo novém zařízení.

Motivace pro jeho standardizaci v 3GPP vycházela z globálního rozšíření GSM a následné potřeby uniformní, bezpečné metody ochrany modulu identifikace účastníka. Zavedením povinného nebo uživatelsky aktivovatelného PINu systém přidal významný deterrent proti běžné krádeži a neautorizovanému použití. Řešil omezení závislosti pouze na fyzickém formátu SIM karty jako bezpečnostním tokenu. Před takovým ověřením byla bezpečnost zcela síťově orientovaná (např. na základě [IMSI](/mobilnisite/slovnik/imsi/) a Ki), ponechávající lokální rozhraní mezi uživatelem a zařízením nechráněné.

Historicky CHV stanovil základní princip mobilní bezpečnosti: koncept dvoufaktorového ověření pro přístup ke službám, kombinující 'něco, co máte' (SIM kartu) s 'něco, co znáte' (PIN). Toto byl klíčový krok v bezpečnosti mobilních služeb pro spotřebitele, podporující důvěru uživatelů a umožňující pokročilé služby, které uchovávají osobní data na SIM. Jeho vytvoření bylo hnáno potřebou chránit síťového operátora proti fraudu a účastníka proti narušení soukromí a finanční ztrátě, vytvářející esenciální komponent celkového modelu důvěry pro digitální mobilní komunikace.

## Klíčové vlastnosti

- Lokální ověření uživatele prostřednictvím verifikace PINu na UICC/SIM
- Ochrana citlivých souborů karty (např. telefonní seznam, SMS) proti neautorizovanému přístupu
- Konfigurovatelný pokusový čítač s blokováním po nadměrných neúspěchách
- Integrace s PUK (PIN Unblocking Key) pro bezpečné zotavení z blokovaného stavu
- Standardizovaná sada příkazů (VERIFY, CHANGE CHV, UNBLOCK CHV) dle ISO/IEC 7816-4
- Podpora více CHV klíčů (např. CHV1 pro uživatele, CHV2 pro administrativní funkce)

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance

---

📖 **Anglický originál a plná specifikace:** [CHV na 3GPP Explorer](https://3gpp-explorer.com/glossary/chv/)
