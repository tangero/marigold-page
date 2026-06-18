---
slug: "sccf"
url: "/mobilnisite/slovnik/sccf/"
type: "slovnik"
title: "SCCF – Subscriber Content Charging Function"
date: 2025-01-01
abbr: "SCCF"
fullName: "Subscriber Content Charging Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sccf/"
summary: "SCCF je účtovací funkce v rámci online účtovacího systému 3GPP, která umožňuje účtování v reálném čase na základě obsahu pro služby účastníků, jako jsou multimediální stahování nebo přístup k prémiové"
---

SCCF je funkce online účtovacího systému 3GPP, která umožňuje účtování v reálném čase na základě obsahu pro služby účastníků uplatňováním politik založených na typu obsahu, objemu nebo době trvání.

## Popis

Subscriber Content Charging Function (SCCF) je součást online účtovacího systému ([OCS](/mobilnisite/slovnik/ocs/)) 3GPP, definovaná k usnadnění účtování v reálném čase na základě obsahu, k němuž mají účastníci přístup. Funguje tak, že komunikuje s aplikačními servery nebo poskytovateli obsahu za účelem přijímání účtovacích událostí souvisejících se specifickými službami, jako je streamování videa, stahování hudby nebo hraní her. SCCF vyhodnocuje tyto události vůči profilům účastníků a předdefinovaným účtovacím pravidlům, aby stanovila cenu, přičemž uplatňuje politiky, které mohou zohledňovat faktory jako typ obsahu, objem dat, dobu trvání relace nebo kvalitu služby. To operátorům umožňuje implementovat flexibilní, detailní účtovací modely odpovídající hodnotě doručovaného obsahu.

Z architektonického hlediska je SCCF součástí širšího rámce OCS, který zahrnuje funkce jako Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)) a Account Balance Management Function ([ABMF](/mobilnisite/slovnik/abmf/)). Komunikuje pomocí standardizovaných protokolů, jako je Diameter, konkrétně referenčního bodu Ro, za účelem výměny účtovacích informací s síťovými prvky. Když účastník zahájí službu založenou na obsahu, aplikační server odešle účtovací požadavek do SCCF, která následně provede rezervaci kreditu, ocenění a aktualizaci zůstatku v reálném čase. Tím je zajištěno, že účastníci jsou účtováni přesně a okamžitě, což brání úniku výnosů a podporuje předplacené i postplacené fakturační scénáře.

Klíčové komponenty uvnitř SCCF zahrnují databázi účtovacích pravidel, která ukládá politiky pro různé typy obsahu, a rating engine, který vypočítává poplatky na základě tarifních plánů. Její role sahá až k podpoře služeb založených na předplatném, kde spravuje opakované poplatky, a k účtování na základě událostí pro jednorázové transakce. Integrací se systémy řízení politik může SCCF také vynucovat výdajové limity nebo nabízet propagační slevy, čímž zlepšuje uživatelský zážitek. Tato funkcionalita je klíčová pro moderní mobilní sítě, kde služby založené na obsahu představují významný zdroj příjmů.

## K čemu slouží

SCCF byla zavedena ve 3GPP Release 5, aby řešila rostoucí potřebu sofistikovaných účtovacích mechanismů, jak se mobilní sítě rozšiřovaly mimo hlasové služby a nabízely různé obsahové služby jako video, hudbu a aplikace. Předchozí účtovací systémy byly často omezeny na jednoduché modely založené na čase nebo objemu, které nedostatečně zachycovaly hodnotu prémiového obsahu. SCCF tento problém řeší tím, že umožňuje účtování s ohledem na obsah, což operátorům dovoluje diferencovat ceny na základě toho, k čemu účastníci přistupují, a tím maximalizovat příležitosti k výnosům.

Její vznik byl motivován vzestupem služeb mobilních dat a poptávkou po účtování v reálném čase pro podporu předplacených modelů a prevenci podvodů. Poskytnutím standardizované funkce v rámci [OCS](/mobilnisite/slovnik/ocs/) SCCF usnadňuje interoperabilitu mezi síťovými prvky a poskytovateli obsahu, čímž řeší omezení proprietárních účtovacích řešení, která brzdila inovace služeb. Tento vývoj podpořil obchodní modely operátorů přecházejících na sítě plně založené na IP, kde se doručování obsahu stalo klíčovou nabídkou.

## Klíčové vlastnosti

- Umožňuje účtování v reálném čase na základě obsahu pro služby účastníků
- Integruje se s OCS pomocí protokolů Diameter přes rozhraní Ro
- Uplatňuje účtovací politiky založené na typu obsahu, objemu nebo době trvání
- Podporuje předplacené i postplacené fakturační scénáře
- Interaguje s aplikačními servery pro spouštění účtovacích událostí
- Dynamicky spravuje rezervaci kreditu a aktualizaci zůstatku

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CTF – Charging Trigger Function](/mobilnisite/slovnik/ctf/)
- [ABMF – Accounting Balance Management Function](/mobilnisite/slovnik/abmf/)

## Definující specifikace

- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [SCCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sccf/)
