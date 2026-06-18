---
slug: "puk"
url: "/mobilnisite/slovnik/puk/"
type: "slovnik"
title: "PUK – PIN Unblocking Key"
date: 2025-01-01
abbr: "PUK"
fullName: "PIN Unblocking Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/puk/"
summary: "Tajný kód používaný k odblokování karty SIM/USIM, když byl osobní identifikační kód (PIN) zadán příliš mnohokrát nesprávně, čímž došlo k zamčení karty. Obnovuje přístup ke službám karty bez vymazání u"
---

PUK je tajný kód sloužící k odblokování zamčené karty SIM/USIM po příliš mnoha chybných zadáních PINu, který obnoví přístup ke službám bez vymazání uložených dat.

## Popis

Klíč pro odblokování PINu ([PIN](/mobilnisite/slovnik/pin/) Unblocking Key, PUK) je bezpečnostní prvek integrovaný do karty UICC (Universal Integrated Circuit Card), která hostuje aplikaci [SIM](/mobilnisite/slovnik/sim/) (Subscriber Identity Module) nebo [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module). Jeho primární funkcí je obnovit přístup k UICC poté, co byl uživatel uzamčen kvůli opakovanému chybnému zadání osobního identifikačního kódu (PIN). Samotný PIN chrání přístup k funkcím UICC, jako je připojení k síti nebo přístup k uloženým kontaktům. Po konfigurovatelném počtu neúspěšných pokusů o zadání PINu (obvykle 3) se UICC dostane do stavu 'PIN-blocked', což znemožní její normální činnost.

Z architektonického hlediska je PUK osmiciferný kód, který je odlišný od PINu a je do UICC předprogramován operátorem během personalizace. Je bezpečně uložen v souborovém systému karty, často v souboru [EF](/mobilnisite/slovnik/ef/)_AD (Administrative Data). PUK není určen pro každodenní použití a je zpravidla poskytován účastníkovi odděleně od PINu, často vytištěn na držáku karty nebo sdělen zabezpečeným kanálem. Proces zahrnuje zadání PUKu uživatelem přes rozhraní zařízení, následované zadáním nového PINu a jeho ověřením. Pokud je PUK zadán správně, resetuje počítadlo pokusů o PIN a umožní nastavit nový PIN, čímž se karta odblokuje.

Pokud je sám PUK zadán nesprávně určitý počet opakování (obvykle 10), dostane se UICC do trvalého stavu 'PUK-blocked'. V tomto stavu je karta nepoužitelná pro přístup k síti, protože nevratně zablokuje bezpečnostní funkce. Jediným řešením je získat novou kartu UICC od mobilního operátora, protože starou nelze obnovit. Tento dvoustupňový bezpečnostní mechanismus (PIN a PUK) vyvažuje uživatelskou přívětivost s ochranou proti útokům hrubou silou. Postup s PUK je standardizován v dokumentu 3GPP TS 31.101 (rozhraní UICC-terminál) a souvisejících specifikacích, což zajišťuje interoperabilitu napříč zařízeními a sítěmi.

## K čemu slouží

PUK byl vytvořen, aby řešil kritický problém použitelnosti vlastní zabezpečení založené na PINu: nevyhnutelnost uživatelské chyby. Bez mechanismu obnovy by zapomenutí PINu nebo opakované chyby při zadávání (např. dítětem) trvale zamklo cenný hardwarový token ([SIM](/mobilnisite/slovnik/sim/) kartu), což by vyžadovalo fyzickou výměnu a způsobilo přerušení služeb. PUK poskytuje bezpečnou 'záchrannou síť', která legitimním uživatelům umožňuje znovu získat kontrolu nad svým předplatným a zařízením.

Historicky, jak se mobilní zařízení stala osobními úložišti dat a identity, stala se bezpečnost SIM karty prvořadou. [PIN](/mobilnisite/slovnik/pin/) byl zaveden, aby zabránil neoprávněnému použití v případě ztráty nebo krádeže zařízení. Čistě trestající mechanismus uzamčení byl však komerčně a prakticky nepřijatelný. PUK tento problém řeší tím, že nabízí jednorázovou cestu k obnově, která zachovává bezpečnost. Je to kompromis, který odrazuje od náhodného hádání (díky samostatnému, delšímu kódu PUK a jeho vlastnímu limitu pokusů) a zároveň poskytuje operátorům zvládnutelný proces zákaznické podpory. Jeho vytvoření bylo motivováno potřebou učinit silné zabezpečení přístupu k zařízení a síti (prostřednictvím PINu) přijatelným a praktickým pro miliony běžných uživatelů, čímž umožnilo masové přijetí funkcí zamykání SIM karet.

## Klíčové vlastnosti

- Osmiciferný tajný kód používaný k odblokování karty UICC (SIM/USIM) zamčené PINem
- Předprogramován mobilním operátorem během personalizace karty
- Resetuje počítadlo pokusů o PIN a umožňuje nastavit nový PIN
- Má vlastní počítadlo pokusů (obvykle 10); jeho překročení trvale zablokuje kartu
- Bezpečně uložen v souborovém systému karty UICC (např. v EF_AD)
- Standardizovaný postup definovaný v 3GPP TS 31.101 a souvisejících specifikacích

## Související pojmy

- [PIN – Personal Identification Number](/mobilnisite/slovnik/pin/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [PUK na 3GPP Explorer](https://3gpp-explorer.com/glossary/puk/)
