---
slug: "lsm"
url: "/mobilnisite/slovnik/lsm/"
type: "slovnik"
title: "LSM – Limited Service Mode"
date: 2025-01-01
abbr: "LSM"
fullName: "Limited Service Mode"
category: "Mobility"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/lsm/"
summary: "Provozní stav UE, ve kterém má přístup pouze k tísňovým službám a případně k dalším zákonem vyžadovaným službám, jako jsou varování před zemětřesením a tsunami. Nastává při selhání běžné registrace a"
---

LSM je provozní stav UE, který umožňuje pouze tísňová volání a některé zákonem vyžadované služby; nastává při selhání běžné registrace, aby bylo zajištěno tísňové spojení bez platného předplatného nebo v zakázané síti.

## Popis

Limited Service Mode (LSM) je definovaný stav uživatelského zařízení (UE) v sítích 3GPP, který je primárně upraven bezpečnostní specifikací 33.401. V tomto režimu je přístup UE k síťovým službám výrazně omezen. Zachovanou klíčovou schopností je možnost iniciovat tísňová volání (např. 112, 911). V závislosti na místních předpisech a konfiguraci sítě může být UE také povoleno přijímat specifické nekomerční služby, jako jsou zprávy systému veřejného varování (PWS), které zahrnují varovný systém pro zemětřesení a tsunami (ETWS) a výstražný systém Commercial Mobile Alert System ([CMAS](/mobilnisite/slovnik/cmas/)). UE je výslovně znemožněn přístup ke všem ostatním běžným komerčním telekomunikačním službám, jako jsou hlasová volání, SMS nebo datové relace.

UE přechází do LSM v důsledku specifických procedur správy mobility. Nejčastějším spouštěčem je neúspěšný pokus o registraci nebo aktualizaci polohy, kdy síť žádost UE odmítne s příčinou označující stav „omezené služby“. K tomu může dojít, pokud se UE nachází v zakázané oblasti polohy nebo sledovací oblasti, pokud má neplatné nebo chybějící předplatné (např. bez SIM karty nebo s neznámým [IMSI](/mobilnisite/slovnik/imsi/)), nebo pokud se pokouší zaregistrovat v síti, která nemá roamingovou dohodu s jejím domovským operátorem. Po obdržení takového odmítnutí přejde entita správy mobility ([MM](/mobilnisite/slovnik/mm/)) nebo správy spojení ([CM](/mobilnisite/slovnik/cm/)) UE do LSM. V tomto stavu UE obvykle přestane provádět běžné periodické aktualizace registrace, ale bude dále vyhledávat vhodné buňky, na kterých by se mohla připojit za účelem tísňového přístupu.

V LSM UE provádí výběr a převýběr buňky, aby se připojila na přijatelnou buňku, ale kritéria jsou ve srovnání s režimem běžné služby uvolněná. UE se musí připojit na buňku, která patří k veřejné pozemní mobilní síti (PLMN) považované za přijatelnou pro tísňová volání – často jde o PLMN s nejvyšší prioritou ze seznamu dostupných sítí. UE si tento připojený stav udržuje, aby monitorovala kanál pro volání pro případná oznámení ETWS/CMAS a byla připravena zahájit proceduru navázání tísňového hovoru. Vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) může být v režimu nečinnosti nebo navázat spojení specificky pro tísňovou službu. Stav LSM zajišťuje soulad s předpisy pro tísňový přístup a veřejnou bezpečnost a poskytuje kritickou funkci záchranného prostředku bez ohledu na stav předplatného uživatele nebo jeho polohu.

## K čemu slouží

Limited Service Mode byl vytvořen za účelem splnění kritických regulatorních a bezpečnostních požadavků vyžadovaných zákonem ve většině zemí: zaručení přístupu k tísňovým službám pro jakoukoli osobu s mobilním zařízením bez ohledu na její vztah s operátorem mobilní sítě. Bez LSM by bylo UE s neplatnou SIM kartou, předplatným mimo pokrytí nebo v zakázané roamingové oblasti zcela nepoužitelné, neschopné vytočit ani tísňová čísla. To představuje významné riziko pro veřejnou bezpečnost.

Před formalizací takových režimů byly implementace ad-hoc a neinteroperabilní. LSM standardizuje chování UE a zajišťuje konzistentní a spolehlivý tísňový přístup napříč všemi zařízeními a sítěmi vyhovujícími standardům 3GPP. Řeší problém, jak se má UE chovat, když je pro běžné komerční účely efektivně „mimo službu“, ale musí stále plnit svou roli potenciálního záchranného prostředku. Režim pečlivě vyvažuje tento přístup s bezpečností a integritou sítě tím, že striktně omezuje dostupné služby a brání neoprávněnému využívání síťových prostředků pro netísňové účely.

LSM navíc zahrnuje doručování vládou nařízených zpráv veřejného varování (ETWS/[CMAS](/mobilnisite/slovnik/cmas/)). Toto rozšíření jeho účelu reflektuje skutečnost, že v situacích katastrof nemusí mít jednotlivci platné předplatné, ale přijetí život zachraňujících výstrah je stejně důležité jako uskutečnění tísňového volání. LSM se tak vyvinul z jednoduchého konceptu „pouze tísňová volání“ na standardizovaný stav podporující minimální soubor zákonem vyžadovaných služeb, který zajišťuje univerzální dostupnost funkcí veřejné bezpečnosti v ekosystému 3GPP.

## Klíčové vlastnosti

- Omezuje UE na tísňová volání a zákonem vyžadované služby, jako jsou výstrahy ETWS/CMAS.
- Spouštěn odmítnutím síťové registrace se specifickými příčinami hodnot označujícími „omezenou službu“.
- UE provádí výběr/připojení buňky na PLMN přijatelné pro přístup k tísňové službě.
- Pozastavuje běžné periodické aktualizace registrace během trvání režimu.
- Zajišťuje soulad s předpisy pro univerzální tísňový přístup.
- Definované chování brání zneužití síťových prostředků pro netísňovou komunikaci.

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [LSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsm/)
