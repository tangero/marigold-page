---
slug: "dema"
url: "/mobilnisite/slovnik/dema/"
type: "slovnik"
title: "DEMA – Differential Electromagnetic Analysis"
date: 2025-01-01
abbr: "DEMA"
fullName: "Differential Electromagnetic Analysis"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/dema/"
summary: "DEMA je technika útoku postranním kanálem, která analyzuje elektromagnetické emise kryptografického hardwaru za účelem extrakce tajných klíčů. Měří nepatrné odchylky v elektromagnetickém záření během"
---

DEMA je technika útoku postranním kanálem, která analyzuje elektromagnetické emise kryptografického hardwaru za účelem extrakce tajných klíčů měřením variací během operací.

## Popis

Diferenciální elektromagnetická analýza (DEMA) je sofistikovaná metoda fyzického útoku, která spadá do širší kategorie útoků postranním kanálem. Na rozdíl od tradiční kryptoanalýzy, která cílí na matematické slabiny algoritmů, DEMA zneužívá neúmyslný únik informací z fyzické implementace kryptografických systémů. Tato technika konkrétně měří a analyzuje elektromagnetické ([EM](/mobilnisite/slovnik/em/)) záření emitované integrovanými obvody, procesory nebo jinými hardwarovými komponentami během provádění kryptografických operací, jako je šifrování, dešifrování nebo generování digitálních podpisů. Tato emise koreluje s interními zpracovávanými daty, včetně tajných klíčů a mezihodnot, což útočníkům umožňuje statisticky odvodit citlivé informace.

Technický základ DEMA zahrnuje sběr elektromagnetických stop pomocí specializovaného vybavení, typicky vysokorychlostního osciloskopu spolu s blízkopolní EM sondou umístěnou v blízkosti cílového zařízení. Sonda zachycuje přechodná elektromagnetická pole generovaná tokem proudu v čipu během výpočtu. Zaznamenává se více stop, zatímco zařízení zpracovává známé nebo zvolené vstupy. Útočník poté na tyto stopy aplikuje statistické metody, nejčastěji techniky Diferenční analýzy spotřeby ([DPA](/mobilnisite/slovnik/dpa/)) adaptované pro EM signály. Porovnáním skutečných EM měření s předpovědními modely toho, jak by se zařízení mělo chovat pro různé hypotézy klíče, může útočník identifikovat správný tajný klíč prostřednictvím korelačních špiček.

V rámci ekosystému 3GPP je DEMA obzvláště relevantní pro hodnocení bezpečnosti univerzálních čipových karet (UICC), včetně [SIM](/mobilnisite/slovnik/sim/) karet, vestavěných SIM (eSIM) a bezpečných prvků uvnitř uživatelského zařízení (UE) a síťové infrastruktury. Specifikace 3GPP TS 35.934 poskytuje metodiky a požadavky pro testování odolnosti proti takovým útokům. Analýza cílí na kryptografické algoritmy standardizované 3GPP, jako je sada algoritmů MILENAGE používaná v autentizaci a dohodě klíče ([AKA](/mobilnisite/slovnik/aka/)), stejně jako další symetrické a asymetrické algoritmy implementované v hardwaru. Úspěšný útok DEMA by mohl kompromitovat dlouhodobý tajný klíč (K) uložený na UICC, čímž by podkopal celý autentizační rámec sítě.

Role DEMA v bezpečnosti 3GPP je primárně obranná. Stanovuje kritické hodnotící kritérium pro hardwarové bezpečnostní moduly, zabezpečené procesory a čipové karty používané v mobilních sítích. Výrobci a certifikační orgány používají testování DEMA, jak je uvedeno v TS 35.934, k posouzení zranitelnosti produktů před nasazením. Opatření proti DEMA zahrnují jak hardwarové, tak softwarové techniky. Hardwarová protiopatření zahrnují návrh na úrovni obvodů, jako jsou filtry napájecího zdroje, elektromagnetické stínění, vyvážené logické styly a náhodné načasování provádění operací. Softwarová protiopatření zahrnují algoritmické maskování, kde jsou mezihodnoty skryty náhodnými daty, a randomizaci prováděcí cesty. Pochopení a zmírnění hrozeb DEMA je nezbytné pro zajištění komplexní bezpečnosti na fyzické vrstvě sítí 5G a budoucích, ochranu soukromí uživatelů a integrity sítě před odhodlanými fyzickými útočníky.

## K čemu slouží

DEMA, jako koncept definovaný a řešený v rámci standardů 3GPP, existuje pro proaktivní identifikaci a zmírnění kritické třídy fyzických bezpečnostních hrozeb proti infrastruktuře mobilních sítí a uživatelským zařízením. Před formálním uznáním takových útoků postranním kanálem se bezpečnostní hodnocení primárně zaměřovala na logické zranitelnosti a zranitelnosti na úrovni protokolu. Matematická síla kryptografických algoritmů, jako je [AES](/mobilnisite/slovnik/aes/) nebo sada MILENAGE, byla považována za dostatečnou. Reálné implementace v křemíku však byly shledány jako propouštějící informace prostřednictvím fyzických kanálů, jako je spotřeba energie, časování a elektromagnetické emise. To vytvořilo významnou mezeru mezi teoretickou a praktickou bezpečností, což umožnilo útočníkům s fyzickým přístupem obejít silnou kryptografii měřením těchto nezamýšlených vedlejších účinků.

Konkrétním problémem, který DEMA řeší, je extrakce tajných kryptografických klíčů z hardwarových bezpečnostních modulů, [SIM](/mobilnisite/slovnik/sim/) karet a základnových procesorů neinvazivními prostředky. Útočník nemusí rozbalovat čip ani používat drahé zařízení s fokusovaným iontovým svazkem; může jednoduše umístit sondu poblíž zařízení během jeho činnosti. To činí útok proveditelným pro širší spektrum protivníků. Motivací pro jeho zařazení do standardů 3GPP (TS 35.934) byla rostoucí hodnota mobilní komunikace, nástup mobilních finančních služeb a potřeba robustní identity zařízení a autentizace v éře IoT. Pokud lze základní tajný klíč na SIM nebo TPM naklonovat prostřednictvím DEMA, kompromituje to identitu uživatele, umožňuje síťový podvod a podkopává důvěru v mobilní sítě jako platformu pro kritické služby.

Historicky byly limity předchozích bezpečnostních přístupů v jejich abstrakci od fyzické reality. Standardy předpokládaly 'black box' model, kde byl algoritmus prováděn dokonale v izolaci. DEMA a související analýzy postranních kanálů ukázaly, že implementace je součástí bezpečnostního obvodu. Standardizací metodiky útoku (DEMA) ve verzi Rel-12 poskytlo 3GPP společný rámec pro výrobce, testovací laboratoře a operátory k hodnocení odolnosti, což vedlo k bezpečnějším hardwarovým návrhům. To bylo obzvláště důležité, jak se sítě vyvíjely směrem k 5G, vyžadující silnější záruky pro síťové segmenty, masivní IoT a ultra-spolehlivou komunikaci s nízkou latencí, které všechny závisí na odolných bezpečnostních prvcích odolných proti manipulaci.

## Klíčové vlastnosti

- Neinvazivní technika útoku vyžadující fyzickou blízkost, ale nikoli zničení zařízení
- Zneužívá korelaci mezi elektromagnetickou emisí a interním zpracováním dat
- Cílí na hardwarové implementace kryptografických algoritmů 3GPP (např. MILENAGE, AES)
- Využívá statistickou diferenciální analýzu na sebraných datech EM stop
- Definována pro bezpečnostní hodnocení a testování dle specifikace 3GPP TS 35.934
- Pohání implementaci hardwarových a softwarových protiopatření v zabezpečených čipech

## Definující specifikace

- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [DEMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dema/)
