---
ID: 2499
author: Patrick Zandl
categories:
- UMTS
- 3G
- Turboúvod do mobilních sítí
layout: post
oldlink: 'https://www.marigold.cz/item/3gpp-release-8-system-architecture-evolution-sae-a-evolved-packet-core-epc-v-ramci-lte-siti

  '
post_date: 2012-09-13 18:16:47
post_excerpt: ''
published: true
summary_points:
- LTE Release 8 navazuje na Release 7 rozšířením modulačního schématu a DC HSPA.
- LTE sítě využívají výhradně IP provoz, což je odlišuje od 3G sítí.
- SAE je systém požadavků, EPC je odpověď na tyto požadavky v Release 8.
- EPC zahrnuje SGW, PGW, MME a PCRF, klíčové komponenty pro fungování LTE.
title: 3GPP Release 8 -  System Architecture Evolution (SAE) a Evolved Packet Core
  (EPC) v rámci LTE sítí
---

<p>Počátky LTE můžeme oprávněně spatřovat v Release 8, která byla vydána z kraje roku 2008 a v mnoha ohledech navazovala na Release 7, zejména rozšířením modulačního schématu 64QAM do použití s MIMO anténami a pak dual-carrier HSPA, DC HSPA, kdy lze pro přenos dat přes HSPA využít dva přenašeče a tedy fakticky zdvojnásobit poskytovanou rychlost (nikoliv kapacitu). Až potud je Release 8 jen logickým vývojem <a href="/item/vysokorychlostni-data-hspa-aneb-3gpp-release-7">Release 7</a>.</p>
<!--more-->

<p>Již v rámci Release 7 vznila Studie proveditelnosti, která měla ověřit vývoj směrem k tomu, co se později nazvalo LTE. Vznikl něco jako rámec, zásady - snůška toho, co bychom my, lidé od počítačů, asi považovali za samozřejmé, ale telekomunikačním harcovníkům to přišlo jako hereze. V rámci LTE totiž měl vzniknout výhradně IP provoz. Pamatujeme si jistě, že klasická 3G/UMTS sít operovala ve dvou režimech: okruhově a paketově spínaném, mezi což se snažila <a href="/item/turbouvod-do-umts-ims-aneb-ip-multimedia-subsystem">vsunout IP Multimedia Subsystem</a>, který měl schizma pocházející ze současného provozu dvou protichůdných technologií nějak zaintegrovat. V rámci Feasibility study se mimo jiné ukázalo, že nejlepším východiskem z dualistického schismatu je oprostit se od jednoho a neb data jsou cloumák, přidržet se dat - a tedy celé LTE postavit nad IP technologií, jako paketově spínanou sít.</p>

<h2>System Architecture Evolution (SAE) a [[Evolved Packet Core](/mobilnisite/epc-evolved-packet-core-lte/)](/mobilnisite/epc-evolved-packet-core-lte/) ([[EPC](/mobilnisite/epc-evolved-packet-core-lte/)](/mobilnisite/epc-evolved-packet-core-lte/)) v rámci LTE sítí</h2>
<p>Jedním z pojmů, ke kterému bychom se v rámci LTE sítí měli prokousat v první řadě, je tandem <em>SAE - EPC</em>. Občas se doslechnu, že jde o synonyma. Nejde, i když si to nadále můžete myslet, není to velká chyba. Když se přemýšlelo o dalším vývoji mobilních sítí v rámci 3GPP konsorcia, přemyšlování šlo i do jádra sítě, tedy do toho, co jsme si v UMTS sítích uvykli označovat za Core Network.</p>

<p>I tady by se mohlo ledasco změnit, soudili moudří pánové a začalo se zkoumat, co. Tak vznikl pracovní úkol (Work Item) v rámci 3GPP nazvaný <strong>System Architecture Evolution</strong>, jehož úkolem bylo zamyslet se nad tím, jak by jádro sítě mělo být do budoucna koncipováno zejména s ohledem na zvyšování přenosových rychlostí, nárůst kapacity, optimalizaci odezvy a pokles významu telefonních služeb i obecnou propojitelnost systémů. Výsledkem těchto úvah byl návrh <strong>Evolved Packet Core</strong> (EPC). A to je také vztah mezi SAE a EPC - zatímco SAE je systém požadavků, EPC je jednou z odpovědí na tyto požadavky (a jediným standardem v rámci 3GPP). I proto jsme si uvykli považovat SAE a EPC za synonyma, dnes ovšem převažuje správné pojmenování EPC, zatímco SAE se používá ve starší literatuře, která vznikala v době, kdy se teprve úkol SAE rozpracovával. Ještě si připomeňme, že EPC se stalo součástí 3GPP standardu v Release 8.</p>

<p>EPC je již dosti plochá struktura založená na IP protokolu a na tom, že co není potřeba centralizovat, jest decentralizováno. Důležité je tedy zejména ono rozšíření podpory IP vrstvy na všechny strany, moderně řečeno <em>end-to-end</em>. Už není žádný výstup do okruhového spínání, jak jej zajištovalo v 3G IMS respektive samotná okruhově spínaná doména. S čímž souvisí také to, že přenos hlasu se v rámci LTE dostal poněkud na vedlejší kolej, počítalo se s ním spíše v rámci další specifikace a také vznikl mechanismus vypuzení hlasového hovoru zpět do WCDMA/2G sítě (fallback) - což UMTS k vlastní škodě nemělo. Je třeba říct, že odříznutím hlasu si LTE ušetřilo hodně práce a také hodně starostí, na druhou stranu si očekávání příchodu hlasu přes VoIP (pamatujme si zkratku <strong>VoLGA</strong> - Voice over LTE via Generic Access) logicky vynutilo řízení kvality přenosu dat přes QoS - místy se celému mechanismu řízení datového toku také říká Quality of Experience, QoE.</p>

<p><img src="/assets/epc-cn1.png" alt="Zjednodušení Core Network na EPC" width="500" height="269" border="0" /></p>

<p><em>Na obrázku je vidět zjednodušení architektury i datových toků, jehož se dosáhlo při přechodu z konstrukce Core Network (Jádra sítě) u UMTS/3G k Evolved Packet Core. Autorem obrázku je Motorola. </em></p>

<p>Důležitým bodem pro EPC je důsledné oddělení roviny přenosu dat a obslužných informací, čímž se redukují prodlevy v přenosu dat (snižuje latence).</p>

<p>S tím souvisí další významná změna týkající se řízení přístupu a účtování služeb. Ta byla v konceptech 2G/3G sítí spojena s konkrétní mobilkou (UE) a její autentizací do sítě. Nově se uplatňuje všeprostupující komponenta <strong>Policy and Charging Rules Function</strong> (PCRF), který transparentně kontroluje a řídí všechny datová spojení a navazuje je na patřičné účtovací mechanismy. To umožňuje mnohem větší kreativitu stran účtování, jehož základem už nutně nemusí být SIM karta nebo objem přenesených dat či čas - například lze účtovat stažení jednoho URL.</p>

<p>Co všechno se stalo součástí EPC? Vlastně všechno, co není v rámci rádiového rozhraní E-UTRAN.</p>

<p>EPC obsahuje následující komponenty:</p>

<ul>
<li>Serving Gateway (SG-W) - Obslužná brána</li>
<li>Packet Data Network (PDN) Gateway (PGW) - Brána sítě paketových dat</li>
<li>Mobility Management Entity (MME) - Entita správy mobility</li>
<li>Policy and Charging Rules Function (PCRF) - Funkce pravidel přístupu a účtování</li>
</ul>
<p>Zatímco SGW, PGW a MME byly poprvé představeny v rámci [[3GPP Release 8](/item/3gpp-release-8-system-architecture-evolution-sae-a-evolved-packet-core-epc-v-ramci-lte-siti/)](/item/3gpp-release-8-system-architecture-evolution-sae-a-evolved-packet-core-epc-v-ramci-lte-siti/), PCFR pochází již z <a href="/item/vysokorychlostni-data-hspa-aneb-3gpp-release-7">předchozí Release 7</a>, ale příliš se neuplatňovala a převažoval původní koncept autentizace mobilky. Od Release 8 je začlenění PCRF a jeho interoperabilita s bránami EPC a MME povinná a bez ní není možné v LTE fungovat.</p>

<p>Na obrázku je vidět schéma LTE sítě s EPC, klasickou GSM/UMTS sítí a sítí CDMA. </p>

<p><img src="/assets/epc-lte.png" alt="EPC v LTE síti" width="500" height="317" border="0" /></p>

<h3>SGW</h3>
<p>Obslužná brána je rozhraním mezi jednotlivými eNodeB a samotným jádrem sítě, konkrétně rozhraním k PGW, bráně sítě paketových dat. Pokud se uživatel pohybuje mezi eNodeB, pořád vstupuje do jádra sítě přes stejnou SGW (což může ovšem znamenat i to, že jich více v síti není) - tomu se říká Mobilní Kotva. Mobilní ukotvení je důležité při výstupu do ne-LTE sítě, jako jsou 2G/3G, kde SGW zprostředkovává mobilní rozhraní, nebo při přerušení připojení třeba za pohybu.</p>

<p>SGW má na starosti uživatelskou rovinu přenosu dat a je také zodpovědná za handovery mezi sousedními eNodeB. Monitoruje a spravuje si kontext informací spojených s mobilkou během klidového režimu a je zodpovědná za vyvolání mobilky, když pro ni dorazí data (někdo ji volá, sestavuje se směrem k ní datové spojení. A samozřejmě i v případě, když spojení k mobilce je přerušeno, je starostí SGW zreplikovat uživatelský přenos dat.</p>

<h3>PGW- Brána sítě paketových dat</h3>
<p>Brána sítě paketových dat (PGW) je koncovým bodem pro paketová data přenášená v rámci sítě paketových dat, technicky řečeno ukončuje SGi rozhraní vůči PDN. Pokud mobilka přistupuje do více paketových sítí, činí tak přes více PGW, ovšem s tím omezením, že není podporováno simultánní připojení přes S5/S8 a Gn/Gp, tedy simultánní komunikace mezi sítěmi 3GPP a ne-3GPP. Česky řečeno, nemůžete v jednu chvíli používat přístup přes LTE a přes WiMax, otázka by také mohla znít, proč byste tak měli chtít činit. <br />V rámci PGW je uskutečňováno řízení přístupu, filtrování paketů pro uživatele, účtování a za tím účelem kontaktuje PCRF, aby zjistilo, jaké oprávnění konkrétní uživatel má a předávalo zúčtovací informace. PGW odpovídá entitě GGSN v architektuře pre-Release8.</p>

<h3>MME - Mobile Management Entity</h3>
<p>Tento prvek jádra sítě dostal mystický přídomek entity - entita. Proč? Protože jde o další (a vlastně klíčový) všeprostupující prvek sítě LTE, který má na starosti řízení mobilního provozu. Stará se o signalizační a řídící funkce důležité pro připojení mobilky (UE) do sítě, přidělení zdrojů sítě a řízení mobility mobilky v síti, tedy o vyvolávání mobilky (paging), roaming a handover. MME se stará o všechny funkce řídící úrovně vztažené ke správě uživatelů a připojení (sessions). Kvůli tomu mu podléhají všechny základnové setanice eNodeB a to je také základní odlišnost LTE proti konceptům 2G/3G sítí, kde se o to starala platforma RNC/SGSN.</p>

<p>Mezi hlavní funkce MME patří:</p>

<ul>
<li>bezpečnostní postupy, především autentikace koncového uživatele, iniciace a sjednávání šifrování i integrita ochranných algoritmů. </li>
<li>řízení sezení (sessions) mezi mobilkou a sítí, týká se to všech signalizačních procedur používaných k sestavení paketového datového konextu a vyjednání s tím souvisejících parametrů, jako je QoS. </li>
<li>Management polohy mobilky ve stavu Idle: sledování jejího pohybu v oblasti a aktualizační proces, díky němuž může být mobilka sítí vyvolána a sestaveno příchozí spojení. </li>
</ul>
<h3><br /> Policy and Charging Rules Function (PCRF) - Funkce pravidel přístupu a účtování</h3>
<p>Už víme, že PCRF bylo představeno jako shrnující funkce pro účtování a řízení přístupu ke službám v Release 7, kde shrnulo Policy Decision Function (PDF) a Charging Rules Function (CRF) z předchozích dvou release. Důvodem tohoto sjednocení nebyla ani tak rychlost (na tu to vliv vlastně nemá), ale potřeba vyřešení řízení přístupu a účtování k sítím mimo 3GPP standard, například WiFi, WiMax či CDMA2000. Aplikační Funkce (AF) je dalším síťovým elementem, který má na starosti podporu aplikací vyžadujících dynamická oprávnění a/nebo kontrolu účtování. V modelu IMS zastupoval Aplikační Funkci Proxy Call Session Control Function (P-CSCF).</p>

<h2>Tok dat v rámci LTE</h2>
<p>Když už jsme se ponořili do jádra sítě, podívejme se tedy ještě pro jistotu, kudy všudy data z mobilky (UE) v rámci LTE sítě putují, abychom také pochopili, kde mohou být zádrhele a jejich neoblíbená forma zvaná zpoždění.</p>

<ul>
<li>rádio mezi UE a eNodeB</li>
<li>datový nosič mezi eNodeB a SGW (S1)</li>
<li>datový nosič mezi SGW a PGW (S5)</li>
</ul>
<p>Na obrázku je to vidět o něco názorněji <em>(autor nákresu je Alcatel)</em>: </p>

<p><img src="/assets/tok-dat-lte.png" alt="Tok dat v rámci LTE sítě" width="500" height="176" border="0" /></p>

<p>Je třeba znovu a důrazně si připomenout, že EPC je velmi významná změna (ne-li nejvýznamnější) v přístupu k mobilním komunikacím, v níž okruhové spínání plně nahrazuje spínání paketové, tedy dochází k implementaci přístupu All-IP.</p>

<p>Mnoho diagramů rozkresluje EPC jako velmi plochou entitu a cudně zamlčuje, že řada krabiček tam prostě musí být, pokud chcete účtovat, autentizovat a provádět další úkony, které jsou z hlediska uživatele pravda často zbytné, ale z hlediska provozovate podstatné. Jsou rovněž definovány přechodové mechanismy umožnující soužití mezi 2G/3G a LTE, což jste z nákresu asi vypozorovali.</p>

<p>Tak a to je asi všechno, co byste si v kostce a stručnosti měli o jádru LTE sítě pamatovat.</p>