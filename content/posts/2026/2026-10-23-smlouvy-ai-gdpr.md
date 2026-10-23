---
slug: smlouvy-ai-gdpr
author: Patrick Zandl
categories:
- AI
- Claude
- Anthropic
- GDPR
- Právo
layout: post
post_excerpt: Smíte nahrát smlouvu s dodavatelem do Claude nebo ChatGPT? Co na to GDPR, NIS2, obchodní tajemství a NDA, co slibuje Anthropic v tarifech Team a Enterprise a proč bezpečné používání AI začíná firemními pravidly, ne dražší licencí.
summary_points:
  - Běžnou obchodní smlouvu lze do schváleného firemního Claude Team nebo Enterprise vložit, pokud máte právní titul, posíláte jen nezbytný obsah a NDA předání nebrání
  - Anthropic na obsahu z Team, Enterprise a API netrénuje, výjimkou je hodnocení palcem, které může vlastník organizace vypnout
  - Data se ukládají v USA, volba „jen EU“ chybí a standardní smluvní doložky nenahrazují posouzení rizik přenosu
  - NIS2 (zákon č. 264/2025 Sb.) se týká jen poskytovatelů regulovaných služeb, Enterprise nevyžaduje
title: "Smlouvy, AI, GDPR - můžete smlouvy a osobní údaje nahrávat do Claude nebo ChatGPT?"
thumbnail: https://www.marigold.cz/assets/smlouvy-ai-gdpr.jpg
---

*Nákupčí nahraje do Claude nebo ChatGPT smlouvu s dodavatelem a chce seznam sankcí a výpovědních lhůt. Ve smlouvě jsou jména jednatelů, podpisy, telefony a neveřejné ceny. Porušil tím GDPR? Vyzradil obchodní tajemství? A zachránil by ho dražší tarif? Odpověď zní, že takové nahrání může být v pořádku. Rozhoduje ale příprava firmy a tu si u žádného předplatného nekoupíte.*

## TLDR

- **Běžnou obchodní smlouvu lze do schváleného firemního Claude Team nebo Enterprise vložit**, pokud máte právní základ pro práci s osobními údaji, odesíláte jen nezbytný obsah a NDA či jiná mlčenlivost předání nebrání.
- **Souhlas každé osoby uvedené ve smlouvě ani schválení úřadem obvykle nepotřebujete.** Potřebujete jednoduchá firemní pravidla, schválené pracovní prostředí a informované zaměstnance.
- **Anthropic na obsahu z Team, Enterprise a API standardně netrénuje.** Výjimkou je hodnocení palcem: celá konverzace se uloží na pět let a může jít do tréninku. Vlastník organizace ho může vypnout.
- **Data se ukládají v USA, smluvní volba „jen EU“ chybí.** Pro přenos se používají standardní smluvní doložky, které však nenahrazují posouzení konkrétních rizik včetně možného přístupu amerických úřadů.
- **Enterprise přidává auditní logy, SCIM, role a vlastní retenci dat.** Problém s NDA ani se zvláštními kategoriemi údajů nevyřeší a vyžaduje minimálně 20 míst.
- **Zdravotní údaje a další zvláštní kategorie do běžného nasazení nepatří.** Ve standardní zpracovatelské smlouvě (DPA) nejsou sjednány.
- **NIS2 (zákon č. 264/2025 Sb.) se týká jen poskytovatelů regulovaných služeb**, a to tam, kde AI zasahuje do aktiv v rozsahu řízení kybernetické bezpečnosti.

České ani evropské právo nezakazuje vkládat osobní údaje do generativní AI. Obecné povolení ale také neexistuje, ani když dodavatel slibuje soulad s GDPR. Posuzuje se konkrétní zpracování: k čemu, v jakém rozsahu, komu data jdou a s jakým rizikem. U smlouvy se k tomu přidávají ještě dvě samostatné otázky. Smíte obsah předat třetí straně? A spadáte pod zákon o kybernetické bezpečnosti? Text se týká soukromých firem s Claude Team, Enterprise nebo přímým API.

*„Chyba není v tom, že zaměstnanec používá AI. Chyba je, když firma neví, jaký nástroj používá a jaké informace do něj odesílá. Bezpečné používání AI začíná jasnými pravidly, nikoli nákupem dražší licence,“ říká [Pavel Martiník](https://martinik.legal), advokát zaměřený na právní regulaci moderních technologií.*

---

## Co Anthropic slibuje

**Netrénuje na vašich datech.** [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) v článku B zakazují Anthropicu trénovat modely na obsahu zákazníka, tedy na vstupech i výstupech. Obsah je automaticky důvěrnou informací a Anthropic ho smí použít jen k plnění smlouvy. Platí to stejně pro Team i Enterprise. Firmy z EU uzavírají smlouvu s irskou pobočkou Anthropic Ireland.

**Trezor to ale není.** K obsahu smějí zaměstnanci a poradci Anthropicu, kteří ho potřebují a jsou vázaní mlčenlivostí. Pokud to vyžaduje zákon nebo soud, Anthropic data vydá a zákazníka o tom informuje, pokud mu to není zakázáno.

**Pro GDPR je klíčová zpracovatelská smlouva.** [Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum) (DPA) v základním nastavení počítá s firmou jako správcem a Anthropicem jako zpracovatelem. Jestliže firma sama jedná jako zpracovatel klientských dat, musí ověřit i oprávnění zapojit dalšího zpracovatele. DPA obsahuje standardní smluvní doložky pro přenos mimo EU a seznam subzpracovatelů. Proti novému subzpracovateli můžete vznést námitku do 15 dnů.

**Smluvní odpovědnost Anthropicu je ve standardních podmínkách omezená** na poplatky za posledních dvanáct měsíců, s výjimkou odškodnění podle smlouvy. To firmu nezbavuje povinností podle GDPR. Sankce ani odpovědnost za konkrétní porušení se však automaticky nepřičítají jen zákazníkovi, posuzuje se role a jednání jednotlivých subjektů.

---

## Celou smlouvu nahrát můžete, obvykle ale nemusíte

**Potřebujete právní titul.** U osob ze smlouvy mezi dvěma firmami jde typicky o oprávněný zájem, případně zákonnou povinnost. Plnění smlouvy je titulem jen vůči osobě, která je smluvní stranou, třeba živnostníkovi. U oprávněného zájmu musíte zvážit nezbytnost a práva dotčených lidí. Pohodlí nákupčího k tomu nestačí. Nový souhlas od každé osoby uvedené ve smlouvě obvykle nepotřebujete: zapojení zpracovatele samo o sobě souhlas nevyžaduje.

**Pošlete jen to, co úkol potřebuje.** K výpovědní lhůtě nejsou potřeba podpisová strana, mobil obchodníka ani číslo účtu. Stačí vybrané články. Když naopak hledáte odpovědnou kontaktní osobu, potřebujete její jméno. Rozsah určuje úkol. Velikost kontextového okna o něm nerozhoduje.

**Přepis „Novák“ na „zaměstnanec 17“ je pouhá pseudonymizace.** Pokud jde člověka znovu určit pomocí klíče nebo kontextu, pořád jde o osobní údaj. Ve smlouvách prozradí identitu i kombinace částky, data a popisu sporu. Údaje navíc musíte odstranit ještě před odesláním. Pokyn „nejdřív tu smlouvu anonymizuj“ už znamená, že jste originál předali. U PDF zkontrolujte i textovou vrstvu, komentáře a metadata.

**Zaměstnance musíte informovat.** [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms) ukládají firmě, aby uživatelům řekla, že pracují ve spravované službě, kde má firma přístup k jejich konverzacím. Zároveň za ně musí zajistit potřebná oznámení a souhlasy. To lze snadno přehlédnout.

---

## Obchodní tajemství a NDA jsou samostatná překážka

GDPR chrání lidi. Neveřejné ceny nebo technický návrh mohou být chráněné i v dokumentu, ze kterého zmizela všechna jména.

Ochrana obchodního tajemství podle [§ 504 občanského zákoníku](https://e-sbirka.gov.cz/sb/2012/89) předpokládá, že vlastník utajení odpovídajícím způsobem zajišťuje. Předání pod smluvní mlčenlivostí tajemství automaticky nezničí. Rozhoduje ale, jak a komu ho předáváte.

U NDA rozhoduje její konkrétní text. Pokud zakazuje předání externím poskytovatelům bez písemného souhlasu, Claude ji neobejde. Na tom nic nemění, že je Anthropic pro účely GDPR „jen“ zpracovatelem.

*„Zpracovatelská smlouva s poskytovatelem AI není univerzální povolení předávat cizí důvěrné informace. NDA je vždy potřeba vyhodnotit samostatně,“ upozorňuje Pavel Martiník.*

Advokáti mají navíc zákonnou mlčenlivost. Česká advokátní komora ve svém [stanovisku z roku 2023](https://advokatnidenik.cz/2023/09/15/stanovisko-cak-k-vyuzivani-ai-pri-poskytovani-pravnich-sluzeb/) jasně uvádí, že odpovědnost za ochranu klientských dat nese vždy advokát. Závěry pro firemní nákup proto na advokátní spis nepřenášejte.

---

## Kam data odcházejí

[Anthropic uvádí](https://privacy.claude.com/en/articles/7996890-where-are-your-servers-located-do-you-host-your-models-on-eu-servers), že data ukládá v USA a zpracování může směrovat do zemí v USA, Evropě, Asii a Austrálii. Bezpečnostní kontroly a podpora mohou probíhat i jinde. Enterprise si může zapnout zpracování výhradně v USA. Volbu „jen EU“ v podmínkách nenajdete.

GDPR přenos mimo EU nezakazuje, vyžaduje ale odpovídající mechanismus. Základem jsou zde standardní smluvní doložky, jejich podpis však sám o sobě nenahrazuje posouzení rizik konkrétního přenosu. Právě mezinárodní předávání dat patří k nejcitlivějším místům celé konstrukce. Evropský sbor pro ochranu osobních údajů ve svých [doporučeních k doplňkovým opatřením](https://www.edpb.europa.eu/documents/recommendation/recommendations-012020-on-measures-that-supplement-transfer-tools-to_en) výslovně řeší případ, kdy poskytovatel potřebuje data v otevřené podobě a hrozí přístup úřadů třetí země. Šifrování s klíči u poskytovatele tento problém neřeší. A jazykový model text číst prostě musí.

U běžných obchodních dokumentů může být po individuálním posouzení takové zbytkové riziko přijatelné. U citlivějších dat je poctivým výsledkem posouzení menší výřez, jiná architektura, nebo nepoužití služby.

---

## Retence a dvoje zadní vrátka

**Zákaz trénování neznamená mazání.** Konverzace v Team i Enterprise zůstávají uložené, abyste v nich mohli pokračovat. Po smazání zmizí ze serverů do 30 dnů. Obsah, který automatika označí za porušení pravidel, se uchovává až dva roky a jeho klasifikační skóre až sedm let ([podrobnosti](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)).

**Enterprise umí vlastní retenci** s minimem 30 dnů. Pozor na projekty: bez vlastního nastavení mohou zůstávat uloženy bez automatického vymazání a jejich retence má přednost před retencí konverzací uvnitř. Nastavení se navíc nevztahuje na Claude Design, Claude Tag, Managed Agents ani na Claude Code běžící v cloudu ([dokumentace](https://privacy.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans)).

**Prvními zadními vrátky je palec nahoru.** Když uživatel ohodnotí odpověď, Anthropic uloží celou související konverzaci až na pět let a smí ji použít i k trénování. Smlouva to v článku o zpětné vazbě připouští. Vlastník organizace ale může hodnocení v Team i Enterprise vypnout volbou Rate chats v nastavení dat a soukromí ([nápověda](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)). „Ve firmě, která do Claude posílá smlouvy, bych hodnocení palcem vypnul hned první den,“ doporučuje Pavel Martiník.

**Druhými jsou nejsilnější modely.** Modely třídy Mythos, a tedy i Fable 5 a 5.1, vede Anthropic jako Covered Models. Vstupy i výstupy si u nich ponechává 30 dní k bezpečnostní kontrole a označený obsah může vidět úzká skupina schválených lidí ([detail](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)). Standardně to platí i při nastavené nulové retenci (ZDR), pokud Anthropic výslovně neschválí výjimku. Firemní chat se ukládá tak jako tak, změna proto dopadá hlavně na firmy, které přes API nebo Claude Code jedou se ZDR. Kdo navíc zapne Development Partner Mode, souhlasí s trénováním na svých datech. Volba modelu tedy patří do firemní směrnice.

---

## Co k tomu přidává český NIS2

Zákon č. [264/2025 Sb., o kybernetické bezpečnosti](https://nukib.gov.cz/cs/infoservis/aktuality/2372-ohlaseni-podle-noveho-zakona-o-kyberneticke-bezpecnosti-provedlo-pres-4800-organizaci/) platí od listopadu 2025 a dopadá na poskytovatele regulovaných služeb podle vyhlášky č. 408/2025 Sb. Samotné používání cloudové AI firmu pod zákon nepřivede.

U regulované firmy rozhoduje, zda AI zasahuje do aktiv v rozsahu řízení kybernetické bezpečnosti. Generátor marketingových textů do něj typicky nespadá, nástroj napojený na provozní dokumentaci energetiky naopak ano. V takovém případě musíte posoudit dodavatele: přístup k datům, součinnost při incidentu, kontrolu plnění a ukončení služby. Podrobnosti stanoví vyhlášky č. 409/2025 Sb. pro vyšší režim a 410/2025 Sb. pro nižší.

NÚKIB v [důvodové zprávě](https://portal.nukib.gov.cz/storage/uploads/2025/12/03/duvodova-zprava-vyhlaska-vyssi-rezim_uid_69303a3e441fc.pdf) počítá i s tím, že velký dodavatel úpravy smlouvy odmítne. Pak to musíte zapsat do hodnocení rizik a vypořádat. Obecné oprávnění požadavky přeskočit z toho neplyne. Tvrzení „NIS2 vyžaduje Enterprise“ proto neplatí. Auditní logy z Enterprise se hodit mohou, posouzení ale nenahradí.

---

## Team, nebo Enterprise

| Oblast | Team | Enterprise |
| - | - | - |
| Smluvní ochrana obsahu (Commercial Terms, DPA) | Ano | Ano, stejná |
| SSO | Ano | Ano |
| SCIM a role s jemnými oprávněními | Ne | Ano |
| Auditní logy a Compliance API | Ne | Ano |
| Vlastní retence | Ne | Ano, s výjimkami |
| Vypnutí hodnocení palcem | Ano | Ano |
| Zpracování pouze v EU | Ne | Ne |
| Cena | od 20 USD/místo | 20 USD/místo + spotřeba za ceny API, min. 20 míst |

Ceny a funkce podle [ceníku](https://claude.com/pricing) k 20. 10. 2026. Ceny Team platí při ročním placení.

Enterprise dává nástroje k vynucování pravidel a kontrole. Pokud vám ale brání NDA nebo nevyřešený přenos do USA, vyšší tarif problém neodstraní. Pro malou firmu s pěti lidmi je navíc minimum dvaceti míst samo o sobě argumentem proti.

---

## Hraniční případy

Následující tabulka je návrh firemní politiky pro situace, které běžný semafor (viz závěr) nepokryje. Zákonný seznam povolených dokumentů neexistuje.

| Dokument nebo úkol | Postup |
| - | - |
| Smlouva pod NDA | Nejdřív ověřit, zda NDA předání externí službě dovoluje |
| Mzdy a personalistika | Omezit rozsah a přístupy; mzda patří mezi běžné osobní údaje, ochranu ale vyžaduje |
| Data klienta, pro kterého jste zpracovatelem | Ověřit, zda vás klient opravňuje zapojit dalšího zpracovatele |
| Provozní dokumentace regulované služby | Posoudit podle zákona o kybernetické bezpečnosti |

Posouzení vlivu na ochranu osobních údajů (DPIA) nepotřebujete ke každému dotazu. Povinné je tehdy, pokud je pravděpodobné, že konkrétní zpracování povede k vysokému riziku pro práva lidí ([EDPB](https://www.edpb.europa.eu/topics/accountability-and-compliance-tools/data-protection-impact-assessment_en)).

---

## Co si z toho odnést

**Doporučení pro firmy: jeden schválený firemní účet a jednoduchý AI semafor.**

**ZELENÁ:** veřejné materiály, vlastní obecné texty a skutečně anonymizované vzory. Ve schváleném firemním prostředí běžně povolit.

**ORANŽOVÁ:** obchodní smlouvy, interní podklady, neveřejné ceny a běžné osobní údaje. Nejprve ověřit oprávnění k předání, vybrat jen nutné části a postupovat podle schvalovacího režimu firmy.

**ČERVENÁ:** hesla a produkční přístupy, zvláštní kategorie osobních údajů nebo důvěrné informace, které nesmíte předat. Nevkládat bez zvláštního právního a bezpečnostního posouzení, u přístupových údajů vůbec.

*„Zaměstnanci nepotřebují ke každému promptu nové právní stanovisko. Potřebují vědět, co smějí vložit sami, co vyžaduje kontrolu a co do externí AI nepatří. To je praktická compliance, která inovace nebrzdí,“ shrnuje Pavel Martiník.*

Bezpečné a doložitelné nasazení stojí na krátké, srozumitelné směrnici, kterou lidé skutečně dodržují, a na přiměřených technických opatřeních. Měla by říkat:

1. **Ve kterém účtu se pracuje.** Firemní e-mail na osobním tarifu Pro totiž firemní smluvní režim nezakládá.
2. **Co se smí nahrát a co se předem odstraní**, podle semaforu a tabulky hraničních případů.
3. **Jaký je právní titul pro zpracování osobních údajů a jak je to s NDA a pokyny klientů.**
4. **Že je hodnocení palcem vypnuté a které modely a konektory jsou povolené.**
5. **Kdo řeší incident.** Pozor, jde o odlišné povinnosti: Anthropic podle DPA oznámí porušení zabezpečení osobních údajů do 48 hodin od svého zjištění. Správce oznamuje porušení ÚOOÚ zpravidla do 72 hodin od svého zjištění, pokud není nepravděpodobné riziko pro práva a svobody osob. Poskytovatel regulované služby hlásí NÚKIB incidenty, na které se vztahuje ohlašovací povinnost, bez zbytečného odkladu, nejpozději do 24 hodin.

Před odesláním dokumentu stačí umět odpovědět na tři otázky: proč potřebujeme právě tento obsah, smíme ho předat externí službě a víme, kde se bude zpracovávat a uchovávat? Pokud odpověď chybí, dokument zmenšete, anonymizujte, nechte schválit, nebo ho neposílejte.

*Stav podmínek a dokumentace k 20. říjnu 2026. Individuálně sjednané smlouvy mohou výsledek změnit. Veřejná správa se řídí pravidly cloud computingu podle zákona č. 365/2000 Sb., finanční instituce nařízením DORA a zdravotnictví vlastními předpisy. Pro ně článek bez dalšího posouzení neplatí. Při změně modelu, funkce nebo podmínek je potřeba parametry ověřit znovu.*
