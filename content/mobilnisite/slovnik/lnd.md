---
slug: "lnd"
url: "/mobilnisite/slovnik/lnd/"
type: "slovnik"
title: "LND – Last Number Dialled"
date: 2025-01-01
abbr: "LND"
fullName: "Last Number Dialled"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lnd/"
summary: "Funkce telefonní služby, která umožňuje uživateli znovu vytočit naposledy volané telefonní číslo, obvykle stisknutím jediného klíče nebo použitím krátkého kódu. Poskytuje pohodlí a urychluje proces op"
---

LND (Last Number Dialled) je funkce telefonní služby, která umožňuje uživateli znovu vytočit naposledy volané telefonní číslo, obvykle stisknutím jediného klíče nebo použitím krátkého kódu.

## Popis

Last Number Dialled (LND) je základní, ale nezbytná doplňková služba v telefonních sítích s komutací okruhů, včetně GSM, UMTS a některých aspektů IMS. Jde o funkci pro koncového uživatele, kterou spravuje mobilní zařízení (Mobilní stanice – [MS](/mobilnisite/slovnik/ms/)) ve spolupráci s podporou sítě. Z funkčního hlediska si MS ukládá naposledy úspěšně vytočené a navázané (či o něj usilované) telefonní číslo do své volatilní či nevolatilní paměti. Když uživatel aktivuje funkci LND – často stisknutím softwarového klávesa pro 'převolání', dedikovaného hardwarového tlačítka nebo krátkého kódu jako *# – MS toto číslo získá a automaticky zahájí nový postup zřizování hovoru.

Z perspektivy síťové architektury je LND primárně funkcí na straně uživatelského zařízení (UE). Jádrová síť ([MSC](/mobilnisite/slovnik/msc/)) není přímo odpovědná za ukládání nebo poskytování naposledy volaného čísla; její úlohou je zpracovat novou žádost o zřízení hovoru, kterou UE vygeneruje. Síť však musí podporovat obecné postupy řízení hovoru (podrobně popsány v 24.008 a dalších specifikacích), které umožňují UE hovor iniciovat. Služba se opírá o standardní signalizační tok pro zřizování [MO](/mobilnisite/slovnik/mo/) hovoru. UE vyplní informační prvek Called Party [BCD](/mobilnisite/slovnik/bcd/) Number v zprávě SETUP uloženým číslem a odešle ji síti.

Fungování je přímočaré, ale zahrnuje koordinaci mezi uživatelským rozhraním ([MMI](/mobilnisite/slovnik/mmi/)) telefonu a jeho vrstvou řízení hovoru. Vrstva řízení hovoru zaznamenává cílové číslo z úspěšně iniciovaného MO hovoru. K tomuto zaznamenání obvykle dochází, když UE odešle do sítě zprávu SETUP. Některé implementace mohou ukládat i čísla z pokusů o hovor, které se nepodařilo navázat. Po aktivaci převolání MMI požádá vrstvu řízení hovoru o uskutečnění hovoru na uložené číslo. Řízení hovoru pak pokračuje standardními postupy autentizace, šifrování a navazování hovoru, jako kdyby uživatel číslo vytočil ručně. Jednoduchost funkce zastiňuje její užitečnost, neboť odstraňuje nutnost ručního opětovného zadávání, snižuje chyby a zlepšuje uživatelský zážitek, zejména u často kontaktovaných čísel nebo po neúspěšném pokusu o hovor.

## K čemu slouží

Funkce LND byla vytvořena jako odpověď na potřebu uživatelského pohodlí a efektivity v raných i pozdějších generacích buněčných sítí. V éře fyzických klávesnic a před rozšířením sofistikovaných seznamů kontaktů bylo ruční vytáčení dlouhých telefonních čísel (zejména mezinárodních) časově náročné a náchylné k chybám. Pokud hovor selhal kvůli přetížení, špatnému pokrytí nebo špatnému číslu, musel uživatel celou sekvenci zadat znovu. Funkce LND tento problém vyřešila automatizací procesu převolání jediným úkonem.

Její zavedení v Rel-5, jako součást širší sady doplňkových služeb GSM/UMTS, odráželo snahu průmyslu zlepšit uživatelský zážitek ze základní hlasové služby. Řešila jasné omezení předchozích ručních způsobů vytáčení. I když se zdála triviální, byly takové funkce klíčové pro přijetí a spokojenost uživatelů na konkurenčních telekomunikačních trzích. Motivací bylo udělat telefon 'chytřejším' a uživatelsky přívětivějším, tedy snížit počet kroků potřebných pro běžné úkony.

I když se sítě vyvíjely směrem k VoIP a volání založenému na IMS, funkce převolání zůstala základním prvkem uživatelského rozhraní telefonu, ačkoli její implementace se stala zcela závislou na koncovém zařízení. V kontextu IMS provádí klient [SIP](/mobilnisite/slovnik/sip/) [UA](/mobilnisite/slovnik/ua/) na zařízení podobnou funkci zaznamenávání a převolání pro SIP [URI](/mobilnisite/slovnik/uri/) nebo tel URI. Funkce LND tak představuje raný a trvalý příklad služby zaměřené na uživatele, navržené k minimalizaci úsilí a maximalizaci užitečnosti hlasové komunikační služby.

## Klíčové vlastnosti

- Ukládá naposledy úspěšně vytočené telefonní číslo do paměti UE
- Po aktivaci uživatelem (např. klávesou Převolání) automaticky zahájí nové zřizování hovoru
- Využívá standardní signalizační postupy pro MO hovor
- Zlepšuje uživatelské pohodlí a snižuje chyby při vytáčení
- Jádrová operace nezávislá na síti (funkce centrická k UE)
- Podporována napříč více generacemi telefonie s komutací okruhů

## Související pojmy

- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [eNB – Evolved Node B](/mobilnisite/slovnik/enb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LND na 3GPP Explorer](https://3gpp-explorer.com/glossary/lnd/)
